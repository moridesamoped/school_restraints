'''
Test out your code in an interactive python session (ipython or notebook).
Once you have code that answers the question, paste it in a .py file. When you're
done, see if you can make your code DRY but writing a couple functions.
'''
# What state has most reports? Thoughts?
import pandas 
df = pandas.read_excel('data/restraints_seclusions.xlsx')

# Let's look at California. What district has most reports?
df.loc[(df["State"]== 'CA'), 'District_name'].value_counts()

#What school has the
# highest rate of physical restraints?
df_CA['phys_rate'] = (df_CA.idea_phys_restraints + df_CA.no_dis_phys_restraints)/ df_CA.total_enrollment
df_CA.loc[df_CA.phys_rate == df_CA.phys_rate.max(), 'School_name']
# Of mechanical restraints?
df_CA['mech_rate'] = (df_CA.idea_mech_restraints + df_CA.no_dis_mech_restraints)/ df_CA.total_enrollment

df_CA.loc[df_CA.mech_rate == df_CA.mech_rate.max(), 'School_name']
#
# (hint: sum
# across both types of students. What else do you need to calculate a rate?)

# Look at data definitions tab in excel file. Let's compare the different types
# of restraints (mechanical v. physical) for disabled and non-disabled students.

# Look at the Propublica_dirty column. How many schools had "dirty" data?
# Do the answers to the above look any different if we exclude these schools?
df_CA.loc[(df_CA.phys_rate == df_CA.phys_rate.max()) & (df_CA.propublica_dirty == 'f'), 'School_name']
df_CA.loc[(df_CA.mech_rate == df_CA.mech_rate.max()) & (df_CA.propublica_dirty == 'f'), 'School_name']

# The ProPublica article says Montgomery County Public Schools have taken action


# on this issue. How can we filter the dataframe down to see schools in this district?
# Hint: look up pandas Series string contains() method.

df.loc[(df.District_name.str.contains('MONTGOMERY')) &  (df.State == 'MD')]

# Bonus: try creating visualization of the different types of restraints used against
# disable/non-disabled students (as above). How might you design this data viz?
