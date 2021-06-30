# Description: This program predicts if a passenger will survive on the titanic

import seaborn as sns
import matplotlib.pyplot as plt

# loading data
titanic = sns.load_dataset('TItanic')
# print the first 10 rows of data
print(titanic.head(10))

# count the number of rows and columns in the data set
print(titanic.shape)

print(titanic.describe())

# get a count of the number of survivors
print(titanic['survived'].value_counts())

dx = sns.countplot(titanic['embarked'], label="Class")
plt.show()

# visualize the number count of survivors
ax = sns.countplot(titanic['survived'], label="Count")
plt.show()

# Visualize the count of survivors for columns who, sex, pclass, sibsp, parch, and embarked
cols = ['who', 'sex', 'pclass', 'sibsp', 'parch', 'embarked']

n_rows = 2
n_cols = 3

# The subplot grid and the figure size of each graph
# This returns a Figure (fig) and an Axes Object (axs)
fig, axs = plt.subplots(n_rows, n_cols, figsize=(n_cols*3.2, n_rows*3.2))

for r in range(0, n_rows):
    for c in range(0, n_cols):

        i = r*n_cols + c  # index to go through the number of columns
        ax = axs[r][c]  # Show where to position each subplot
        sns.countplot(titanic[cols[i]], hue=titanic["survived"], ax=ax)
        ax.set_title(cols[i])
        ax.legend(title="survived", loc='upper right')

plt.tight_layout()
plt.show()

# look at survival rate by sex
print(titanic.groupby('sex')['survived'].mean())
# Look at survival rate by sex and class
print(titanic.pivot_table('survived', index='sex', columns='class'))

# look at survival rate by sex and class visually
titanic.pivot_table('survived', index='sex', columns='class').plot()
plt.show()

# plot the survival rate of each class.
sns.barplot(x='class', y='survived', data=titanic)
plt.show()
