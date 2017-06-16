import sys

if sys.version_info.major < 3:
    int_type = (int, long)
    string_type = (str, unicode)
    def force_text(string):
        if not isinstance(string, string_type):
            return unicode(string)
        if not isinstance(string, unicode):
            return string.decode('utf-8')
        return string
else:
    int_type = (int,)
    string_type = (str, bytes)
    def force_text(string):
        if not isinstance(string, string_type):
            return str(string)
        if not isinstance(string, str):
            return string.decode('utf-8')
        return string
