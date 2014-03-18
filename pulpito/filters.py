import jinja2.filters
import json
from datetime import datetime
import pytz
import tzlocal


local_tz = tzlocal.get_localzone()


def tojson_filter(obj, **kwargs):
    return jinja2.Markup(json.dumps(obj, **kwargs))


def utc_stamp_to_local(stamp, format='%Y-%m-%d %H:%M:%S'):
    utc_dt_naive = datetime.strptime(stamp, format)
    utc_dt_aware = pytz.utc.localize(utc_dt_naive)
    local_dt = utc_dt_aware.astimezone(local_tz)
    return local_dt.strftime(format)


def setup_filters():
    jinja2.filters.FILTERS['localtime'] = utc_stamp_to_local
    if not 'tojson' in jinja2.filters.FILTERS:
        jinja2.filters.FILTERS['tojson'] = tojson_filter
    return True
