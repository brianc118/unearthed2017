from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
import csv

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost/ivms', echo=True)
Session = sessionmaker(bind=engine)


class Alert(Base):
    __tablename__ = 'Alerts'

    AlertId = Column(Integer, primary_key=True)
    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    Drivers_ID = Column(Integer)
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    EventType = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Integer)
    Textbox20 = Column(String(512))
    RoadSpeedLimit = Column(String(512))
    OverspeedLocation = Column(String(512))
    TotalDuration = Column(String(512))
    StartOdo = Column(Float)
    EndOdo = Column(Float)
    F_StartStreet = Column(String(512))
    F_StartSuburb = Column(String(512))
    F_EndStreet = Column(String(512))
    F_EndSuburb = Column(String(512))
    StartLocation = Column(String(512))
    EndLocation = Column(String(512))
    StartLongLat = Column(String(512))
    EndLongLat = Column(String(512))
    FuelUsed = Column(Float)
    Distance = Column(Float)


Base.metadata.create_all(engine)
alert_path = '../data/IVMS Challenge/DATA/IVMS/Alert/'
alert_file = 'ND_Alerts_12_months.csv'

alert_headers = {'AlertId': 'int',
				 'AssetSiteName': 'string',
                 'ReportGroup': 'string',
                 'AssetName': 'string',
                 'AssetExtra': 'string',
                 'Drivers_ID': 'int',
                 'Asset2SiteName': 'string',
                 'Asset2ReportGroup': 'string',
                 'AssetName2': 'string',
                 'AssetExtra2': 'string',
                 'AssetID2': 'int',
                 'EventKey': 'int',
                 'EventDescription': 'string',
                 'EventType': 'string',
                 'EventStartDate': 'string',
                 'EventStartTime': 'string',
                 'EventEndDate': 'string',
                 'EventEndTime': 'string',
                 'TimeZone': 'string',
                 'TotalOccurs': 'int',
                 'EventValue': 'int',
                 'Textbox20': 'string',
                 'RoadSpeedLimit': 'string',
                 'OverspeedLocation': 'string',
                 'TotalDuration': 'string',
                 'StartOdo': 'float',
                 'EndOdo': 'float',
                 'F_StartStreet': 'string',
                 'F_StartSuburb': 'string',
                 'F_EndStreet': 'string',
                 'F_EndSuburb': 'string',
                 'StartLocation': 'string',
                 'EndLocation': 'string',
                 'StartLongLat': 'string',
                 'EndLongLat': 'string',
                 'FuelUsed': 'float',
                 'Distance': 'float'}

alert_order = ['AlertId',
               'AssetSiteName',
               'ReportGroup',
               'AssetName',
               'AssetExtra',
               'Drivers_ID',
               'Asset2SiteName',
               'Asset2ReportGroup',
               'AssetName2',
               'AssetExtra2',
               'AssetID2',
               'EventKey',
               'EventDescription',
               'EventType',
               'EventStartDate',
               'EventStartTime',
               'EventEndDate',
               'EventEndTime',
               'TimeZone',
               'TotalOccurs',
               'EventValue',
               'Textbox20',
               'RoadSpeedLimit',
               'OverspeedLocation',
               'TotalDuration',
               'StartOdo',
               'EndOdo',
               'F_StartStreet',
               'F_StartSuburb',
               'F_EndStreet',
               'F_EndSuburb',
               'StartLocation',
               'EndLocation',
               'StartLongLat',
               'EndLongLat',
               'FuelUsed',
               'Distance']


def cast_types(col_num, val):
    col_type = alert_headers[alert_order[col_num]]
    if val.strip() == '':
        return None
    if col_type == 'int':
        return int(val)
    elif col_type == 'float':
        return float(val.replace(',', ''))
    return val


with open(os.path.join(alert_path, alert_file)) as csvf:
    session = Session()
    rr = csv.reader(csvf, delimiter=',')
    rows = []
    for k, r in enumerate(list(rr)[1:]):
        row_dict = {}
        for i, c in enumerate([str(k + 1)] + r):
            row_dict[alert_order[i]] = cast_types(i, c)
        # print(row_dict)
        rows.append(Alert(**row_dict))
    session.add_all(rows)
    session.commit()
    print('finished upload')
