import numpy as np
import pandas as pd

# load the full data file

df = pd.read_csv('projects.csv')
print(df.columns)
df.insert(7, "Rated Energy", "", True)
df.insert(8, "Duration", "", True)
df.insert(9, "Modular", "", True)

# split projects by battery type
print(df.columns)
#print(df[' Technology Broad Category'].unique())

def separateByTechType(df):
	liIon = df.loc[(df[' Technology Mid-Type']=='Lithium Polymer Battery') | (df[' Technology Mid-Type']=='Lithium-ion Battery') | 
		(df[' Technology Mid-Type']=='Lithium Iron Phosphate Battery') | (df[' Technology Mid-Type']=='Lithium Nickel Manganese Cobalt Battery') | 
		(df[' Technology Mid-Type']=='Lithium Ion Titanate Battery') | (df[' Technology Sub-Type']=='Lithium-ion Battery') | 
		(df[' Technology Sub-Type']=='Lithium Iron Phosphate Battery') | (df[' Technology Sub-Type']=='Lithium Nickel Manganese Cobalt Battery') | 
		(df[' Technology Sub-Type']=='Lithium Ion Titanate Battery')]
	df = df.loc[(df[' Technology Mid-Type']!='Lithium Polymer Battery') & (df[' Technology Mid-Type']!='Lithium-ion Battery') & 
		(df[' Technology Mid-Type']!='Lithium Iron Phosphate Battery') & (df[' Technology Mid-Type']!='Lithium Nickel Manganese Cobalt Battery') & 
		(df[' Technology Mid-Type']!='Lithium Ion Titanate Battery') & (df[' Technology Sub-Type']!='Lithium-ion Battery') & 
		(df[' Technology Sub-Type']!='Lithium Iron Phosphate Battery') & (df[' Technology Sub-Type']!='Lithium Nickel Manganese Cobalt Battery') & 
		(df[' Technology Sub-Type']!='Lithium Ion Titanate Battery')]
	flow = df.loc[(df[' Technology Mid-Type']=='Vanadium Redox Flow Battery') | (df[' Technology Mid-Type']=='Flow Battery') | 
		(df[' Technology Mid-Type']=='Zinc Bromine Flow Battery') | (df[' Technology Sub-Type']=='Zinc Iron Flow Battery') | 
		(df[' Technology Sub-Type']=='Vanadium Redox Flow Battery') | (df[' Technology Sub-Type']=='Zinc Bromine Flow Battery')]
	df = df.loc[(df[' Technology Mid-Type']!='Vanadium Redox Flow Battery') & (df[' Technology Mid-Type']!='Flow Battery') & 
		(df[' Technology Mid-Type']!='Zinc Bromine Flow Battery') & (df[' Technology Sub-Type']!='Zinc Iron Flow Battery') & 
		(df[' Technology Sub-Type']!='Vanadium Redox Flow Battery') & (df[' Technology Sub-Type']!='Zinc Bromine Flow Battery')]
	pb = df.loc[(df[' Technology Mid-Type']=='Lead-acid Battery') | (df[' Technology Mid-Type']=='Valve Regulated Lead-acid Battery') | 
		(df[' Technology Mid-Type']=='Advanced Lead-acid Battery') | (df[' Technology Sub-Type']=='Lead-acid Battery') |
		(df[' Technology Sub-Type']=='Valve Regulated Lead-acid Battery') | (df[' Technology Sub-Type']=='Hybrid Lead-acid Battery/Electro-chemical Capacitor')]
	df = df.loc[(df[' Technology Mid-Type']!='Lead-acid Battery') & (df[' Technology Mid-Type']!='Valve Regulated Lead-acid Battery') & 
		(df[' Technology Mid-Type']!='Advanced Lead-acid Battery') & (df[' Technology Sub-Type']!='Lead-acid Battery') & 
		(df[' Technology Sub-Type']!='Valve Regulated Lead-acid Battery') & (df[' Technology Sub-Type']!='Hybrid Lead-acid Battery/Electro-chemical Capacitor')]
	caes = df.loc[(df[' Technology Mid-Type'] == 'Compressed Air Energy Storage') | (df[' Technology Mid-Type'] == 'Compressed Air Storage') | 
		(df[' Technology Mid-Type'] == 'Liquid Air Energy Storage')]
	df = df.loc[(df[' Technology Mid-Type'] != 'Compressed Air Energy Storage') & (df[' Technology Mid-Type'] != 'Compressed Air Storage') & 
		(df[' Technology Mid-Type'] != 'Liquid Air Energy Storage')]
	ph = df.loc[df[' Technology Broad Category']=='Pumped Hydro Storage']
	df = df.loc[df[' Technology Broad Category']!='Pumped Hydro Storage']
	th = df.loc[df[' Technology Broad Category']=='Thermal Storage']
	df = df.loc[df[' Technology Broad Category']!='Thermal Storage']
	h2 = df.loc[df[' Technology Broad Category']=='Hydrogen Storage']
	df = df.loc[df[' Technology Broad Category']!='Hydrogen Storage']
	otherBat = df.loc[(df[' Technology Mid-Type']== 'Sodium based Battery') | (df[' Technology Mid-Type']== 'Sodium-ion Battery') | 
		(df[' Technology Mid-Type']== 'Metal Air Battery') | (df[' Technology Mid-Type']=='Sodium-sulfur Battery') | 
		(df[' Technology Mid-Type']=='Zinc Air Battery') | (df[' Technology Mid-Type']=='Nickel based Battery') | 
		(df[' Technology Sub-Type']=='Sodium-ion Battery') | (df[' Technology Sub-Type']=='Zinc Manganese Dioxide Battery')]
	df = df.loc[(df[' Technology Mid-Type']!= 'Sodium based Battery') & (df[' Technology Mid-Type']!= 'Sodium-ion Battery') & 
		(df[' Technology Mid-Type']!= 'Metal Air Battery') & (df[' Technology Mid-Type']!='Sodium-sulfur Battery') & 
		(df[' Technology Mid-Type']!='Zinc Air Battery') & (df[' Technology Mid-Type']!='Nickel based Battery') & 
		(df[' Technology Sub-Type']!='Sodium-ion Battery') & (df[' Technology Sub-Type']!='Zinc Manganese Dioxide Battery')]
	cap = df.loc[(df[' Technology Mid-Type']== 'Electro-chemical Capacitor')] 
	df = df.loc[(df[' Technology Mid-Type']!= 'Electro-chemical Capacitor')] 

	liIon.to_csv('outputs/li-ion.csv')
	flow.to_csv('outputs/flow.csv')
	pb.to_csv('outputs/pb.csv')
	caes.to_csv('outputs/caes.csv')
	ph.to_csv('outputs/ph.csv')
	th.to_csv('outputs/th.csv')
	h2.to_csv('outputs/h2.csv')
	otherBat.to_csv('outputs/otherBat.csv')
	cap.to_csv('outputs/cap.csv')
	df.to_csv('outputs/stragglers.csv')
	return(df)

#n = df.loc[df[' Technology Mid-Type'] == 'nan']
df = separateByTechType(df)

# check to see if the csv files have entries that already exist 
def checkPreviousEntries(refDF, newDF):
	


