# Based on https://www.w3.org/TR/tabular-data-primer/datatypes.svg

def integer(value):
    try:
        return int(value)
    except:
        return None

def floatConversion(value):
    try:
        return float(value)
    except:
        return None

def stringConversion(value):
    return value

# def anyAtomicType (value):
# def anyURI(value):
# def base64Binary(value):
# def boolean(value):
# def date(value):
# def dateTime(value):
# def dateTimeStamp(value):
# def decimal(value):
# def long(value):
# def int(value):
# def short(value):
# def byte(value):
# def nonNegativeInteger(value):
# def positiveInteger(value):
# def unsignedLong(value):
# def unsignedInt(value):
# def unsignedShort(value):
# def unsignedByte(value):
# def nonPositiveInteger(value):
# def negativeInteger(value):
# def double(value):
# def double (number)(value):
# def duration(value):
# def dayTimeDuration(value):
# def yearMonthDuration(value):
# def gDay(value):
# def gMonth(value):
# def gMonthDay(value):
# def gYear(value):
# def gYearMonth(value):
# def hexBinary(value):
# def QName(value):
# def normalizedString(value):
# def token(value):
# def language(value):
# def Name(value):
# def NMTOKEN(value):
# def xml(value):
# def html(value):
# def json(value):
# def time(value):

# Functions to convert value from string to specified datatype
metadata_types = {
    'integer': integer,
    'float': floatConversion,
    'string': stringConversion
    # anyAtomicType
    # anyURI
    # base64Binary
    # boolean
    # date
    # dateTime
    # dateTimeStamp
    # decimal
    # long
    # int
    # short
    # byte
    # nonNegativeInteger
    # positiveInteger
    # unsignedLong
    # unsignedInt
    # unsignedShort
    # unsignedByte
    # nonPositiveInteger
    # negativeInteger
    # double
    # double (number)
    # duration
    # dayTimeDuration
    # yearMonthDuration
    # gDay
    # gMonth
    # gMonthDay
    # gYear
    # gYearMonth
    # hexBinary
    # QName
    # normalizedString
    # token
    # language
    # Name
    # NMTOKEN
    # xml
    # html
    # json
    # time
}