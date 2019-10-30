#  _____ _     _       _       ____  _             _     
# |_   _| |__ (_)___  (_)___  |  _ \(_)_ __  _   _| | __ _| |_ ___
#   | | | '_ \| / __| | / __| | |_) | | '_ \| | | | |/ _` | __/ _ \
#   | | | | | | \__ \ | \__ \ |  __/| | |_) | |_| | | (_| | ||  __/
#   |_| |_| |_|_|___/ |_|___/ |_|   |_| .__/ \__,_|_|\__,_|\__\___|
# There are many frameworks like it,  |_| but this one is mine. --MikeL


import pickle
import gspread
import pandas as pd
from sys import stdout
from os import environ
from apiclient.discovery import build
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


global_doc = None


def doc(akey):
    """Creates a global gspread document object for easier pipulating."""
    global global_doc
    global_doc = key(akey)
    sheet1 = global_doc.worksheets()[0].title
    print("Run selections like: cl, df = gs.pipulate('%s', 'A1:D10')" % sheet1)


def pipulate(worksheet, row_or_range, cols=None, columns=None, start=None, end=None):
    """All that pipulate really is"""
    
    tab = check_worksheet(worksheet)

    if cols: 
        row1, row2 = row_or_range
        col1, col2 = cols
        col1, col2 = a1(col1, reverse=True), a1(col2, reverse=True)
        cl = tab.range(row1, col1, row2, col2)
        list_of_lists = cl_to_list(cl)
        if not columns:
            cell_list = tab.range(row1, col1, row1, col2)
            columns = [a1(x.col) for x in cell_list]
        print('cl, df = pipulate("%s", %s, %s) << SUCCESSFUL! >>' % (tab.title, row_or_range, cols))
    else:
        cl = tab.range(row_or_range)
        list_of_lists = cl_to_list(cl)
        if not columns:
            columns = [a1(i+1) for i, x in enumerate(list_of_lists[0])]
        print('cl, df = pipulate("%s", "%s") << SUCCESSFUL! >>' % (tab.title, row_or_range))

    df = pd.DataFrame(list_of_lists, columns=columns)
    print("You may now manipulate the DataFrame but maintain its (%s x %s) shape." % df.shape)
    print('To update the GSheet with changes, gs.populate("%s", cl, df)' % tab.title)
    return cl, df


def populate(worksheet, cl, df):
    """Push df back to spreadsheet."""

    tab = check_worksheet(worksheet)

    if cl_df_fits(cl, df):
        lol = df.values.tolist()
        flat = [y for x in lol for y in x]
        flat[:] = ['N/A' if pd.isnull(x) else x for x in flat]
        for i, cell in enumerate(cl):
            cell.value = flat[i]
        tab.update_cells(cl)
    else:
        raise SystemExit()
    print('gs.populate(tab, cl, df) <<< GSHEET UPDATED! >>>')


def check_worksheet(worksheet):
    if type(worksheet) == gspread.models.Worksheet:
        tab = worksheet
    elif type(worksheet) == str:
        if 'global_doc' in globals():
            if worksheet in [x.title for x in global_doc.worksheets()]:
                tab = global_doc.worksheet(worksheet)
            else:
                print("Worksheet not found")
                raise SystemExit()
        else:
            print("gs.doc([Your GSheets key here]) must be set")
            raise SystemExit()
    return tab


def cl_to_list(cl):
    new_table = []
    for i, cell in enumerate(cl):
        if i == 0:
            row_num = 1
            memory = cell.row
            row = [cell.value]
        if cell.row == memory and i > 0:
            row.append(cell.value)
        else:
            row_num += 1
            memory = cell.row
            row = [cell.value]
            new_table.append(row)
    return new_table


def cl_df_fits(cl, df):
    """Check if GSpread cell list same shape as Pandas dataframe."""
    list_of_lists = cl_to_list(cl)
    height = len(list_of_lists)
    width = len(list_of_lists[0])
    size_tuple = (height, width)
    if size_tuple == df.shape:
        return True
    print('GOOGLE SHEET NOT UPDATED.')
    print('cl %s and df %s different sizes.' % (size_tuple, df.shape))
    return False


def a1(pos, reverse=False):
    """Return the column letter for numeric column index."""
    if reverse:
        return gspread.utils.a1_to_rowcol('%s1' % pos)[1]
    if str(pos).isdigit():
        return gspread.utils.rowcol_to_a1(1, pos)[:-1]
    else:
        return "Must be integer"


def link(gsheet_key):
    """Return GSheet URL for data from Web UI."""
    return 'https://docs.google.com/spreadsheets/d/%s/edit' % gsheet_key


def key(key):
    """Alias to Return instance of GSheet by key."""
    global gsprd
    print("View the GSheet at %s" % link(key))
    return gsprd.open_by_key(key)


def analytics():
	return build('analyticsreporting', 'v4', credentials=credentials)


def searchconsole():
	return build('webmasters', 'v3', credentials=credentials)


def ga(gaid, start, end, path):
    """Return Google Analytics metrics for a URL."""

    path = path.replace(',', r'\,')
    service = analytics()
    metrics = ['users', 'newUsers', 'sessions', 'bounceRate',
               'pageviewsPerSession', 'avgSessionDuration']
    metrics = ''.join(['ga:%s,' % x for x in metrics])[:-1]
    ga_request = service.data().ga().get(
        ids='ga:' + gaid,
        start_date=start,
        end_date=end,
        metrics=metrics,
        dimensions='ga:pagePath',
        sort='-ga:users',
        filters='ga:pagePath==' + path,
        segment='sessions::condition::ga:medium==organic',
        max_results=1
    )
    ga_response = ga_request.execute()
    rval = []
    if 'rows' in ga_response:
        raw_rows = ga_response['rows'][0]
        rval = raw_rows
    return rval


def gsc(prop, start, end, query, url):
    service = searchconsole()
    request = {
        "startDate": start,
        "endDate": end,
        "dimensions": [
            "query",
            "page"],
        "dimensionFilterGroups": [
        {
            "filters": [
            {
                "operator": "equals",
                "expression": url,
                "dimension": "page"
            },
            {
                "operator": "equals",
                "expression": query,
                "dimension": "query"
            }]
        }]
    }
    dat = service.searchanalytics().query(siteUrl=prop, body=request).execute()
    val = []
    if 'rows' in dat:  # For the foolish Hobgoblins of PEP8 consistency
        r = dat['rows'][0]
        val = [start] + [r['keys'][0]] + [r['keys'][1]] + [
            r['position']] + [r['clicks']] + [r['impressions']] + [r['ctr']]
    return val


def api_date(a_datetime, time=False):
    """Return datetime string in Google API friendly format."""

    if time:
        return ('{0:%Y-%m-%d %H:%M:%S}'.format(a_datetime))
    else:
        return ('{0:%Y-%m-%d}'.format(a_datetime))


def human_date(a_datetime, time=False):
    """Return datetime object as American-friendly string."""

    if time:
        return ('{0:%m/%d/%Y %H:%M:%S}'.format(a_datetime))
    else:
        return ('{0:%m/%d/%Y}'.format(a_datetime))


def email():
    """Return email given provided Google OAuth account."""
    service = build("oauth2", "v2", credentials=credentials)
    user_document = service.userinfo().get().execute()
    email = user_document['email']
    return email


def login():
    client_id = "769904540573-knscs3mhvd56odnf7i8h3al13kiqulft.apps.googleusercontent.com"
    client_secret = "D2F1D--b_yKNLrJSPmrn2jik"
    environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"
    scopes = ["https://www.googleapis.com/auth/analytics.readonly", 
              "https://www.googleapis.com/auth/webmasters.readonly", 
              "https://www.googleapis.com/auth/yt-analytics.readonly",
              "https://www.googleapis.com/auth/youtube.readonly", 
              "https://spreadsheets.google.com/feeds/", 
              "https://www.googleapis.com/auth/gmail.modify", 
              "https://www.googleapis.com/auth/userinfo.email"] 
    client_config = {
        "installed": {
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
            "client_id": client_id,
            "client_secret": client_secret
        }
    }
    flow = InstalledAppFlow.from_client_config(client_config, scopes)
    credentials = flow.run_console()
    credentials.access_token = credentials.token
    with open("credentials.pickle", "wb") as output_file:
        pickle.dump(credentials, output_file)
    return credentials


def logout():
    import requests
    from os import remove
    global credentials
    requests.post('https://accounts.google.com/o/oauth2/revoke',
        params={'token': credentials.token},
        headers = {'content-type': 'application/x-www-form-urlencoded'})
    try:
        remove('credentials.pickle')
    except:
        pass
    credentials = None


class Unbuffered(object):
    """Provides more real-time streaming in Jupyter Notebook"""

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


try:
    with open("credentials.pickle", "rb") as input_file:
        credentials = pickle.load(input_file)
except:
    credentials = False

if not credentials:
    credentials = login()

if not credentials.valid:
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    credentials.access_token = credentials.token
    with open("credentials.pickle", "wb") as output_file:
        pickle.dump(credentials, output_file)
    if not credentials.valid:
        credentials = login()

gsprd = gspread.authorize(credentials)

print("You are logged in as %s" % email())
print('Get started by running: gs.doc("insert your gsheet key here")')

stdout = Unbuffered(stdout)
