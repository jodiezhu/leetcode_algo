import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("C:/Users/jodie.zhu/Desktop/Book1.csv")
df.columns = ['Date', 'Age','Sex','Health','Education','Family_Income','Employment',
              'Address','Travel_distance','Commute','Transportation','Vehicles',
              'Support_Statements','Multiuse_Trail','Trail_speed','Collision_witness',
              'Speed_limit','multiuselane_propelled','bicyclelane_use','bikelane_propelled',
              'Sidewalk','Personal_mobile']

#clearify values in "Health" column:
df['Health']=df['Health'].replace(['In poor shape, but active & improving',
                                   'Obese, diabetic but trying to be healthy',
                                   'healthy but with arthritis mobilty issues'], 'Fairly poor')

df['Health']=df['Health'].replace(['Back Injury','Disabled','healing fractured heel','need knee replacement'], 'Poor')


#clearify values in "Education" column:
df['Education']=df['Education'].replace(['Grade 8','working towards OSSD'], 'Secondary')

df['Education']=df['Education'].replace(['Grade 9','High school Student','High school diploma '], 'High school')

df['Education']=df['Education'].replace(['College or trade school diploma','college degree (not university and not a diploma)'
                                        ], 'College/Trade/technical/vocational training')

df['Education']=df['Education'].replace(['4 years university, no degree','Some University','Some university',
                                        'University Student','some uni','some university',
                                         'University','university','University degree'], 'University')

df['Education']=df['Education'].replace(['Graduate','Law School','M,D.','PhD'], 'Post graduate')

df['Education']=df['Education'].replace(['Professional degree','Professional Certifications'], 'Professional degree')

df['Education']=df['Education'].replace(['in HS','still in school'], 'Unknown')


#clearify values in "Employment" column:
df['Employment']=df['Employment'].replace(['Contract','Extreme full-time','FT Contract','Full Time','full time casual',
                                          'full time work and student'], 'Employee')

df['Employment']=df['Employment'].replace(['DISABLED ','DISSABLE','Disability pension',
                                          'Doctoral Student','Home Maker','ODSP','Student','disabled',
                                          'ltip disability'], 'Unemployed')

df['Employment']=df['Employment'].replace(['Free Lance','Free-lance and home maker','Freelance Artist',
                                          'Freelance Contractor','Part Time','Seasonal Full-Time','Student/internship',
                                          'arts worker - partial full time','contract','part time while I write',
                                          'occasional teacher','semi-retired self-employed'], 'Worker')

df['Employment']=df['Employment'].replace(['Full time job 3 days a week own startup rest of time',
                                          'Self Employed','Self-employed '], 'Self-employed')

df['Employment']=df['Employment'].replace(['none of your business',
                                           '''I don't understand the rationale for these demographic questions and I'm not sure the privacy statements meets CIMS requirements '''], 'Unknown')

#clearify values in "Address" column:
df['Address']=df['Address'].replace(['Ajax ','Durham','oshawa','Pickering','whitby','durham region','Whitby'], 'GTA')

df['Address']=df['Address'].replace(['Bloor West Village','Central Toronto York or East York',
                                     'Etobicoke','GTA','GTA FOR LIFE!','High Park',
                                     'I used to live in central Toronto still visit for extended periods regularly ',
                                     'KW','North York','Thornhill','west end','never north of bloor downtown ','Scarborough',
                                     'Leslieville','beaches','leaside','Beach','Beaches'], 'Toronto')

df['Address']=df['Address'].replace(['Brampton','mississauga','Mississauga','brampton','mississauga east'], 'GTA')

df['Address']=df['Address'].replace(['Bulington','Burlington','Halton','Oakville','oakville','Milton'], 'GTA')

df['Address']=df['Address'].replace(['YORK REGION','Markham','Richmomd Hill','Vaughan','markham','Woodbridge','Richmond Hill','York Region'], 'GTA')

df['Address']=df['Address'].replace(['out of town','other','Work in TO','not sharing'], 'Unknown')

df['Address']=df['Address'].replace(['Guelph','cambridge','hamilton','Waterloo','niagara region','Hamilton','Barrie',
                                     'St Catharines','i live in hamilton partner lives in north york','Peterborough County',
                                     'Paris Ontario','St Catharines Ontario','Guelph '], 'Southern Ontario')

df['Address']=df['Address'].replace(['Victoria BC','Bangkok','South Africa'], 'Out of Province')

df['Address']=df['Address'].replace(['City of Orillia'], 'Central Ontario')

df['Address']=df['Address'].replace(['Kingston','ottawa','Ottawa'], 'Eastern Ontario')


#clearify values in "Address" column:
df['Transportation']=df['Transportation'].replace(['private motor vehicle (car truck SUV van motorcycle gas limited speed motorcycle or moped)',
                                                   'Motorcycle depends on weather','private motor vehicle','Motorcycle',
                                                   'I cover Ontario for work so Car but in TO- TTC and Bike are easier options',
                                                   'Hybrid Car' ], 'Private Motorized Vehicles')

df['Transportation']=df['Transportation'].replace(['scooter type e-bike','pedal assist type e-bike','Motor scooter',
                                                   'transit in winter otherwise e-bike','pedal assisted scooter type e-bike'], 'ebike')

df['Transportation']=df['Transportation'].replace(['bicycle','bike in summer transit in winter','depends on the season three seasons bike one transit',
                                                   '5000W custom high power electric bicycle (non-scooter)','bike in good weather',
                                                   'Winter TTC Other seasons Bike ','Car in winter bicycle in summer',
                                                   'electric assist bicycle','transit or bicycle (weather dependent)'], 'Bike')

df['Transportation']=df['Transportation'].replace(['transit','transit & bicycle','depends on season Transit in winter e-bike in summer ',
                                                   'CONDO SHUTTLE BUS',], 'Transit')

df['Transportation']=df['Transportation'].replace(['walking','running','skateboard/longboard','personal mobility device (electric wheelchair)',
                                                   'rollerblades','taxi','Cycling/transit highly seasonal 50:50','all',
                                                   'combination of transit and walking'], 'Other')



df.to_csv('C:/Users/jodie.zhu/Desktop/test.csv', index=False)

