{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Diabetes Prediction Using Machine Learning\n",
    "\n",
    "![](https://th.bing.com/th/id/R.93a34add728d3880841fb131262e39aa?rik=YEdot7%2fzIBz1RQ&riu=http%3a%2f%2fraynardsanito.com%2fwp-content%2fuploads%2f2016%2f01%2fDiabetes-Mellitus-.jpg&ehk=%2fo6g3ynPSvGpBgGTzDYH%2f2s84IYYOOpZH5k1ZSgsmms%3d&risl=&pid=ImgRaw&r=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to run the code\n",
    "\n",
    "This tutorial is an executable [Jupyter notebook](https://jupyter.org) hosted on [Jovian](https://www.jovian.ai). You can _run_ this tutorial and experiment with the code examples in a couple of ways: *using free online resources* (recommended) or *on your computer*.\n",
    "\n",
    "#### Option 1: Running using free online resources (1-click, recommended)\n",
    "\n",
    "The easiest way to start executing the code is to click the **Run** button at the top of this page and select **Run on Binder**. You can also select \"Run on Colab\" or \"Run on Kaggle\", but you'll need to create an account on [Google Colab](https://colab.research.google.com) or [Kaggle](https://kaggle.com) to use these platforms.\n",
    "\n",
    "\n",
    "#### Option 2: Running on your computer locally\n",
    "\n",
    "To run the code on your computer locally, you'll need to set up [Python](https://www.python.org), download the notebook and install the required libraries. We recommend using the [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) distribution of Python. Click the **Run** button at the top of this page, select the **Run Locally** option, and follow the instructions.\n",
    "\n",
    ">  **Jupyter Notebooks**: This tutorial is a [Jupyter notebook](https://jupyter.org) - a document made of _cells_. Each cell can contain code written in Python or explanations in plain English. You can execute code cells and view the results, e.g., numbers, messages, graphs, tables, files, etc., instantly within the notebook. Jupyter is a powerful platform for experimentation and analysis. Don't be afraid to mess around with the code & break things - you'll learn a lot by encountering and fixing errors. You can use the \"Kernel > Restart & Clear Output\" menu option to clear all outputs and start again from the top."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## *Work Flow*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> $**First Step**$\n",
    "* Diabeties Data\n",
    "* Data Processing/Cleaning\n",
    "* Exploratory Data Analysis\n",
    "* Train Test Split \n",
    "* Support Vector Machine Classifier\n",
    "> $**Step Two**$\n",
    "* New Data\n",
    "* Support Vector Machine Classifier\n",
    "* Diabetic and Non-Diabetic Prediction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](https://i.ytimg.com/vi/wEo5PdCD5Tk/maxresdefault.jpg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### About The Diseases"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Diabetes mellitus is a condition defined by persistently high levels of sugar (glucose) in the blood. There are several types of diabetes. The two most common are called type 1 diabetes and type 2 diabetes.\n",
    "\n",
    "> During digestion, food is broken down into its basic components. Carbohydrates are broken down into simple sugars, primarily glucose. Glucose is a critically important source of energy for the body’s cells. To provide energy to the cells, glucose needs to leave the bloodstream and get inside the cells.\n",
    "\n",
    "> An organ in the abdomen called the pancreas produces a hormone called insulin, which is essential to helping glucose get into the body's cells. In a person without diabetes, the pancreas produces more insulin whenever blood levels of glucose rise (for example, after a meal), and the insulin signals the body's cells to take in the glucose. In diabetes, either the pancreas's ability to produce insulin or the cells' response to insulin is altered."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "$**Importing Libraries**$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import svm\n",
    "import seaborn as sns\n",
    "from sklearn.metrics import accuracy_score\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Data collection"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`DATASET` : **DIABETES DATASET**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ">Getting the data using the `opendatasets` helper library to download the files from kaggle."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'opendatasets'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [25], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mopendatasets\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mod\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'opendatasets'"
     ]
    }
   ],
   "source": [
    "import opendatasets as od"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'od' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [26], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhttps://www.kaggle.com/datasets/jillanisofttech/diabetes-disease-updated-dataset/download?datasetVersionNumber=1\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m----> 2\u001b[0m \u001b[43mod\u001b[49m\u001b[38;5;241m.\u001b[39mdownload(url)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'od' is not defined"
     ]
    }
   ],
   "source": [
    "url = 'https://www.kaggle.com/datasets/jillanisofttech/diabetes-disease-updated-dataset/download?datasetVersionNumber=1'\n",
    "od.download(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "diabetes_df = pd.read_csv(\"diabetes.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>4</td>\n",
       "      <td>103</td>\n",
       "      <td>60</td>\n",
       "      <td>33</td>\n",
       "      <td>192</td>\n",
       "      <td>24.0</td>\n",
       "      <td>0.966</td>\n",
       "      <td>33</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>461</th>\n",
       "      <td>1</td>\n",
       "      <td>71</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>21.8</td>\n",
       "      <td>0.416</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>365</th>\n",
       "      <td>5</td>\n",
       "      <td>99</td>\n",
       "      <td>54</td>\n",
       "      <td>28</td>\n",
       "      <td>83</td>\n",
       "      <td>34.0</td>\n",
       "      <td>0.499</td>\n",
       "      <td>30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>403</th>\n",
       "      <td>9</td>\n",
       "      <td>72</td>\n",
       "      <td>78</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>31.6</td>\n",
       "      <td>0.280</td>\n",
       "      <td>38</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "35             4      103             60             33      192  24.0   \n",
       "461            1       71             62              0        0  21.8   \n",
       "365            5       99             54             28       83  34.0   \n",
       "403            9       72             78             25        0  31.6   \n",
       "\n",
       "     DiabetesPedigreeFunction  Age  Outcome  \n",
       "35                      0.966   33        0  \n",
       "461                     0.416   26        0  \n",
       "365                     0.499   30        0  \n",
       "403                     0.280   38        0  "
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diabetes_df.sample(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Preparation and Cleaning\n",
    "Let's select a subset of columns with the relevant data for our analysis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(768, 9)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diabetes_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.845052</td>\n",
       "      <td>120.894531</td>\n",
       "      <td>69.105469</td>\n",
       "      <td>20.536458</td>\n",
       "      <td>79.799479</td>\n",
       "      <td>31.992578</td>\n",
       "      <td>0.471876</td>\n",
       "      <td>33.240885</td>\n",
       "      <td>0.348958</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3.369578</td>\n",
       "      <td>31.972618</td>\n",
       "      <td>19.355807</td>\n",
       "      <td>15.952218</td>\n",
       "      <td>115.244002</td>\n",
       "      <td>7.884160</td>\n",
       "      <td>0.331329</td>\n",
       "      <td>11.760232</td>\n",
       "      <td>0.476951</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.078000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>0.243750</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>117.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>30.500000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0.372500</td>\n",
       "      <td>29.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>140.250000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>127.250000</td>\n",
       "      <td>36.600000</td>\n",
       "      <td>0.626250</td>\n",
       "      <td>41.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>199.000000</td>\n",
       "      <td>122.000000</td>\n",
       "      <td>99.000000</td>\n",
       "      <td>846.000000</td>\n",
       "      <td>67.100000</td>\n",
       "      <td>2.420000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "count   768.000000  768.000000     768.000000     768.000000  768.000000   \n",
       "mean      3.845052  120.894531      69.105469      20.536458   79.799479   \n",
       "std       3.369578   31.972618      19.355807      15.952218  115.244002   \n",
       "min       0.000000    0.000000       0.000000       0.000000    0.000000   \n",
       "25%       1.000000   99.000000      62.000000       0.000000    0.000000   \n",
       "50%       3.000000  117.000000      72.000000      23.000000   30.500000   \n",
       "75%       6.000000  140.250000      80.000000      32.000000  127.250000   \n",
       "max      17.000000  199.000000     122.000000      99.000000  846.000000   \n",
       "\n",
       "              BMI  DiabetesPedigreeFunction         Age     Outcome  \n",
       "count  768.000000                768.000000  768.000000  768.000000  \n",
       "mean    31.992578                  0.471876   33.240885    0.348958  \n",
       "std      7.884160                  0.331329   11.760232    0.476951  \n",
       "min      0.000000                  0.078000   21.000000    0.000000  \n",
       "25%     27.300000                  0.243750   24.000000    0.000000  \n",
       "50%     32.000000                  0.372500   29.000000    0.000000  \n",
       "75%     36.600000                  0.626250   41.000000    1.000000  \n",
       "max     67.100000                  2.420000   81.000000    1.000000  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Statistical measurement of the data\n",
    "diabetes_df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 768 entries, 0 to 767\n",
      "Data columns (total 9 columns):\n",
      " #   Column                    Non-Null Count  Dtype  \n",
      "---  ------                    --------------  -----  \n",
      " 0   Pregnancies               768 non-null    int64  \n",
      " 1   Glucose                   768 non-null    int64  \n",
      " 2   BloodPressure             768 non-null    int64  \n",
      " 3   SkinThickness             768 non-null    int64  \n",
      " 4   Insulin                   768 non-null    int64  \n",
      " 5   BMI                       768 non-null    float64\n",
      " 6   DiabetesPedigreeFunction  768 non-null    float64\n",
      " 7   Age                       768 non-null    int64  \n",
      " 8   Outcome                   768 non-null    int64  \n",
      "dtypes: float64(2), int64(7)\n",
      "memory usage: 54.1 KB\n"
     ]
    }
   ],
   "source": [
    "diabetes_df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data contains no nan value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    500\n",
       "1    268\n",
       "Name: Outcome, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The diabetes cases count and non-diabetic\n",
    "\n",
    "diabetes_df['Outcome'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* 0 > Non-Diabetic\n",
    "* 1 > Diabetic\n",
    "> We have 500 people who aren't diabetic and 268 who are diabetic"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The relationship between `columns` and `outcome`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> It is said that during pregnancy, your body makes more hormones and goes through other changes,such as weight gain. These changes cause your body's cells to use insulin less effectively, a condition called insulin resistance. Insulin resistance increases your body's need for insulin."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA+kAAAIoCAYAAAAV/qraAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAA9hAAAPYQGoP6dpAABR6UlEQVR4nO3de3yO9ePH8fdtZzGHbYachmgsYfsqk4SsRlIppHKu5DTWiW8Hh8jhJ1FCfXNIyaGTFKV95RQVLVQOHYSJbTZiYzOzfX5/eLi/3W1ic891bXs9H4/78bjv676ua+/Pbra97891X5fDGGMEAAAAAAAsV8bqAAAAAAAA4BxKOgAAAAAANkFJBwAAAADAJijpAAAAAADYBCUdAAAAAACboKQDAAAAAGATlHQAAAAAAGyCkg4AAAAAgE1Q0gEAAAAAsAlKOgCg2FqwYIEcDofz5unpqRo1aqhv3746dOiQ1fFQSFlZWZo5c6ZuuukmVapUSd7e3rr66qvVrVs3rV+/vsD7279/vxwOhxYsWOD+sAAAuJmn1QEAALhc8+fP17XXXqvMzExt2LBBEydO1Pr16/Xjjz/qqquusjoeCiA1NVW33367fvjhB/Xr109PPvmkKleurEOHDunjjz9W+/btFR8fr+uvv97qqAAAFAlKOgCg2AsLC1NERIQkqW3btsrJydELL7yg5cuX64EHHsh3m4yMDJUtW/ZKxsQl6NWrl3bs2KHVq1erXbt2Ls/16NFDsbGxqlSpkkXpAAAoehzuDgAocW688UZJ0oEDByRJffr0Ubly5fTjjz8qKipK5cuXV/v27SVJZ86c0fjx43XttdfKx8dHQUFB6tu3r1JSUlz2mZWVpccff1xVq1ZV2bJldfPNNys+Pl516tRRnz59nOudPwR/7dq1euyxxxQYGKiAgADdc889Onz4sMs+ly5dqqioKFWrVk1+fn4KDQ3VyJEjderUKZf1zuf/7bff1LFjR5UrV041a9bU448/rqysrDw5x40bp9DQUPn6+iogIEBt27bV5s2bJUnt27fXtddeK2OMy3bGGNWvX1+dOnW64Pf1rrvuUu3atZWbm5vnuRtuuEHNmzd3Pn7vvfd0ww03qEKFCipbtqzq1q2rfv36XXDfkhQfH6/PPvtM/fv3z1PQz/vXv/6lWrVqOR//9NNP6tKliypVqiRfX181bdpUb7311j9+Henc97ROnTp5lo8ZM0YOh8NlmcPh0JAhQzR//nw1bNhQfn5+ioiI0DfffCNjjP7v//5PISEhKleunNq1a6fffvvNZftbbrlFYWFh2rp1q1q3bu38fkyaNMnle5mbm6vx48c7v0bFihXVpEkTzZgx46LjAQCUHJR0AECJc74kBQUFOZedOXNGd955p9q1a6ePP/5YY8eOVW5urrp06aJJkyapZ8+eWrlypSZNmqS4uDjdcsstyszMdG7ft29fTZ8+XX379tXHH3+srl276u6779bx48fzzTBgwAB5eXnp3Xff1ZQpU7Ru3To9+OCDLuv8+uuv6tixo+bOnavPP/9cw4cP17Jly9S5c+c8+8vOztadd96p9u3b6+OPP1a/fv308ssva/Lkyc51zp49q+joaL3wwgu644479NFHH2nBggWKjIxUQkKCJCkmJkY///yz1qxZ47L/zz77THv37tXgwYMv+H3t16+fEhIS9OWXX7os37Nnj7Zs2aK+fftKkr7++mt1795ddevW1ZIlS7Ry5Uo9//zzOnv27AX3LUlffPGFpHNvBlyKn3/+WZGRkdq5c6deeeUVffjhh2rUqJH69OmjKVOmXNI+LtWnn36qN998U5MmTdLixYuVnp6uTp066fHHH9emTZs0c+ZMvfHGG9q1a5e6du2a502QpKQkPfDAA3rwwQe1YsUKRUdHa9SoUXrnnXec60yZMkVjxozR/fffr5UrV2rp0qXq37//Bf+NAQBKKAMAQDE1f/58I8l88803Jjs726Snp5tPP/3UBAUFmfLly5ukpCRjjDG9e/c2ksy8efNctl+8eLGRZD744AOX5Vu3bjWSzKxZs4wxxuzcudNIMk8//XS+2/fu3TtPpkGDBrmsO2XKFCPJJCYm5juW3Nxck52dbdavX28kmR07djifO59/2bJlLtt07NjRNGzY0Pl44cKFRpL5z3/+c8HvWU5Ojqlbt67p0qWLy/Lo6GhTr149k5ube8Fts7OzTXBwsOnZs6fL8qeeesp4e3ub1NRUY4wxU6dONZLM8ePHL7iv/AwcONBIMnv27Lmk9Xv06GF8fHxMQkJCnrGULVvW+fX37dtnJJn58+c71+ndu7epXbt2nn2OHj3a/P3PI0mmatWq5uTJk85ly5cvN5JM06ZNXb5n06dPN5LMDz/84FzWpk0bI8l8++23Lvtt1KiRue2225yP77jjDtO0adNLGjsAoORiJh0AUOzdeOON8vLyUvny5XXHHXeoatWq+uyzzxQcHOyyXteuXV0ef/rpp6pYsaI6d+6ss2fPOm9NmzZV1apVtW7dOklynlG8W7duLtvfe++98vTM//Qud955p8vjJk2aSPrfIfiS9Pvvv6tnz56qWrWqPDw85OXlpTZt2kiSdu/e7bK9w+HIM8PepEkTl/199tln8vX1/cfDysuUKaMhQ4bo008/dc6u7927V59//rkGDRqU51Dvv/L09NSDDz6oDz/8UCdOnJAk5eTk6O2331aXLl0UEBAg6dwh6dK579eyZcuK7Ez7X375pdq3b6+aNWu6LO/Tp48yMjL09ddfu+1rtW3b1uUkhKGhoZKk6Ohol+/Z+eV/fV0kqWrVqmrRooXLsr+/fi1atNCOHTs0aNAgrV69WmlpaW7LDwAoPijpAIBib+HChdq6dau2bdumw4cP64cfflCrVq1c1ilbtqz8/f1dliUnJ+v48ePy9vaWl5eXyy0pKUmpqamSpKNHj0pSntLv6enpLKZ/9/flPj4+kuQ8hP7kyZNq3bq1vv32W40fP17r1q3T1q1b9eGHH7qs99f8vr6+efZ5+vRp5+OUlBRVr15dZcr886/3fv36yc/PT3PmzJEkvfbaa/Lz87voZ8bPb3v69GktWbJEkrR69WolJiY6D3WXpJtvvlnLly/X2bNn1atXL9WoUUNhYWFavHjxP+77/GfN9+3bd9Ec0rnXpVq1anmWV69e3fm8u1SuXNnlsbe39z8u/+vrIuX99yCde/3++jqPGjVKU6dO1TfffKPo6GgFBASoffv2+u6779wyBgBA8UBJBwAUe6GhoYqIiFDTpk3zLW2S8p0hPn9St61bt+Z7mzVrlqT/Fazk5GSX7c+ePVvoIvjll1/q8OHDmjdvngYMGKCbb75ZERERKl++fKH2J537DP7hw4fzPbHbX1WoUEG9e/fWm2++qWPHjmn+/Pnq2bOnKlaseNGv0ahRI7Vo0ULz58+XdO7yd9WrV1dUVJTLel26dNGaNWt04sQJrVu3TjVq1FDPnj3/cXb7tttukyQtX778ojmkc69LYmJinuXnT9AXGBh4wW19fX3znHRPkvONGSt4enoqNjZW33//vY4dO6bFixfr4MGDuu2225SRkWFZLgDAlUVJBwCUWnfccYeOHj2qnJwcRURE5Lk1bNhQ0rmZYenc2dj/6v3337/oydAu5PybBudn2M97/fXXC7U/6dyh16dPn9aCBQsuuu6wYcOUmpqqe++9V8ePH9eQIUMu+ev07dtX3377rb766it98skn6t27tzw8PPJd18fHR23atHGe4G7btm0X3G/z5s0VHR2tuXPn5jk53Xnfffed8zD99u3bO9/s+KuFCxeqbNmyzrP856dOnTo6cuSIyxsvZ86c0erVqy+4zZVUsWJF3XvvvRo8eLCOHTum/fv3Wx0JAHCFcJ10AECp1aNHDy1atEgdO3ZUTEyMWrRoIS8vL/3xxx9au3atunTporvvvluNGzfW/fffr5deekkeHh5q166ddu7cqZdeekkVKlS46OHl+YmMjFSlSpU0cOBAjR49Wl5eXlq0aJF27NhR6PHcf//9mj9/vgYOHKiff/5Zbdu2VW5urr799luFhoaqR48eznUbNGig22+/XZ999pluuukmXX/99QX6OrGxsbr//vuVlZXlcgk6SXr++ef1xx9/qH379qpRo4aOHz+uGTNmuHzm/kIWLlyo22+/XdHR0erXr5+io6NVqVIlJSYm6pNPPtHixYsVHx+vWrVqafTo0fr000/Vtm1bPf/886pcubIWLVqklStXasqUKapQocIFv0737t31/PPPq0ePHnryySd1+vRpvfLKK8rJybnk74O7de7cWWFhYYqIiFBQUJAOHDig6dOnq3bt2rrmmmssywUAuLKYSQcAlFoeHh5asWKF/v3vf+vDDz/U3XffrbvuukuTJk2Sr6+vrrvuOue68+fPV0xMjObOnavOnTtryZIlWrZsmSRd0mHifxcQEKCVK1eqbNmyevDBB9WvXz+VK1cuz2x9QXh6emrVqlUaNWqUPvroI3Xp0kW9evXSV199pdq1a+dZv3v37pJUoFl06dzh8nfffbf++OMPtWrVSg0aNHB5/oYbblBSUpKefvppRUVF6ZFHHpGfn5++/PJLNW7c+B/3HRgYqK+++kpTp07Vjh079NBDD6ldu3YaMWKEMjIytGLFCucbCg0bNtTmzZvVsGFDDR48WHfddZd++uknzZ8/X08++eQ/fp2QkBB9/PHHOn78uO699149+eSTuu+++9SrV68CfS/cqW3bttqwYYMGDhyoDh066Nlnn1X79u21fv16eXl5WZYL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3mVJS0vTiy++qNdee0316tXT0aNHdejQIdWuXVvXX3+9RowYoTZt2lgds0hQ2O3v/J/mvE7Fy99ft+L8Opb0nxPHjx9XxYoVlZubK4fDYcuxlpy3+i22ePFiff7551q3bp127dqlWbNmafbs2Xr++ecVFBSk0aNHa+bMmVbHLLS0tDQdPXpUubm5F1zn5MmTOnXq1BVMdfn27NmjoUOH6qabblLLli0VGRmpLVu2uKyTm5urs2fPWpSw8L755hs99thjGjhwoPr166fHHntMR44c0aJFizR06FAtWrSoWI4rISFBqamp2r9/vzZv3qyXX35Zo0aN0j333KOkpCRt2rRJP/30kzIyMqyOWmALFy7Uq6++6vxlsXPnTj333HOKiYnRqFGjtGnTJosTFt6yZcv08ccfq3r16srKytIbb7yhrl27qn379goNDdX48eOVnp5udcxC+eCDD3TgwAGNGzdOUVFR+umnn6yO5Baff/65RowYoZ07d+q3337T6NGjtWPHDo0YMULXXXedYmJitG/fPqtjFsqSJUu0cuVKbdiwQdu3b9frr7+uFi1aqHPnzjpx4oQGDBigdevWWR3zsmVnZ2vbtm1av369EhISJBXPwlDa2LU0XI7c3FylpaUpMTHR6ihud/53199ft+L8OjocDv36669WxygyI0eO1C+//KIyZcrY9jWipLvJypUr1blzZ0VGRkqSQkJCdOONN6pv375auHChevTooZkzZxbbP2gmTJig3r1765VXXtHGjRv1xx9/KDMz0+Xzim+99ZbGjBljXchCmDhxorPYJSUlqXr16ho3bpwyMjKUk5MjSfrvf/+rZcuWWZy04KZMmaKAgAAlJydr+/btOnz4sPr166enn35au3fv1tixY/X2229bHbPAmjRpoueee07NmjXTypUrNXPmTHXp0kX79u1TuXLlNHfuXPXv319z5syxOmqBffLJJ7rrrrskSStWrFDfvn21YMECHThwQF988YX69etXbIvD8uXLFR0drQoVKmjmzJmaO3eu6tWrpzFjxujee+/VkiVL9J///MfqmIWyZMkSjR49Wp9++qkOHz6su+++W++++66ysrIkyfmzpLiZOXOm2rdvry1btujTTz/V6dOn9fDDD2vXrl3q0aOH1q5dq+nTp0sqfp9d/+STT9S1a1c1a9ZMktSxY0c1adJEFSpU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BlqYsPD+/PNP8/DDDxuHw2F8fX1N06ZNzauvvmqMOffz5f333zeVKlWyOGXhnDlzxkRERJj//Oc/zmXnf2aet2LFCtOwYUOza9euKx3vsmRmZpr69eubt99+26xZs8Y8/vjjpkmTJsbLy8v4+/ubdu3amRdeeMFUqFDBLFmyxOq4l+zUqVMmICAgz+vx5JNPmoiICHPq1CljzLni9M4771gRsdBOnTplKlWq5Px7xBhjvL29zbJly5yPV65caW688cZi+6bY2rVrTePGjV0m4oKDg02vXr1M9+7djb+/v/nyyy8tTFgwJ0+eNA6Hw/ma1a1b16xatcrld9xLL71kIiMjzcGDB62KWSgnT540Xl5e5tChQ85lW7ZsMW3atDHlypUzzz77rG0mQijpReCTTz4xvXv3NiEhISYgIMC0adPGPPnkk85ZzeIoPT3dnDx50hhz7pd9dna2y+E7jz32mLn55putilcoOTk5Zvfu3c5ZoNzcXOcfMuvXrzfNmzc3//rXv0x0dLSVMQslJyfHHD161KSnp19wnSeeeMJ07NjxCqYqGgsXLjRly5Y1ffv2LXbv5v5VTk6OSU5ONl999ZUZP368eeGFF/L88ouNjS2W/x7P+/XXX03Hjh1NmTJljMPhMNddd53p06ePiYiIMNddd52ZOHGi1REL7MyZMyY1NdVlWW5urvONogMHDpguXboUu1k9Y879cf3OO++YQYMGmbVr15rXXnvNtGzZ0nz66afmxRdfNDfccINzJqW4yszMNN98841LOUhISDAjR440Tz75pIXJCi83N9eMGzfOVK1a1axfvz7fdfbt22d8fX2d5a+42Lt3r+nWrVueopqYmGjee+8906dPH1O9enXjcDhMRkaGRSkLbtu2baZ58+bmq6++Msb8b9Lg/Eclp02bZlJTU43D4XD+LVZcbNmyxdxyyy1mz549xhhjDh48aFq1amWOHTvm/Fn5yy+/mOrVqxer1+y886/V/PnzTVRUlNm7d69JTEw0Xl5e5vjx4871itPfJxs2bDAeHh7mnnvuMV27djVXX32180318+P48ccfTa1atUxmZqaVUQts/vz5pmLFisaYvIe1T5kyxTRs2ND069fP/Pnnnxakc0VJL2JZWVkX/Jx6SZGVlWUGDBhg3n77baujuMX5oj58+HDjcDjMokWLLE7kPud/uL7//vsm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tGzZMn3wwQfavn27JKlTp05KSkrSqlWrFB8fr+bNm6t9+/Y6duyYJGnRokWaMGGCJk+erPj4eNWqVSvPrLwkrV27Vnv37tXatWv11ltvacGCBVqwYIHz+TNnzuiFF17Qjh07tHz5cu3bt099+vTJs59nnnlGL730kr777jt5enqqX79+zudWrlype+65R506ddK2bduchT4/xpiLju2BBx5QjRo1tHXrVsXHx2vkyJEl7ugCAEDp4jDGGKtDAACAc/r06aPjx49r+fLlkqQtW7aoY8eOat++vUJDQ/Xiiy/q0KFDzsPCv/zyS9199906cuSIfHx8nPupX7++nnrqKT3yyCO68cYbFRERoZkzZzqfv+mmm3Ty5Eln0e/Tp4/WrVunvXv3ysPDQ5LUrVs3lSlTRkuWLMk369atW9WiRQulp6erXLlyWrdundq2bav//ve/at++vSRp1apV6tSpkzIzM+Xr66vIyEjVrVtX77zzTr77rFOnjoYPH67hw4df0tj8/f316quvqnfv3oX7hgMAYDPMpAMAYDOffvqpypUrJ19fX7Vs2VI333yzXn31VUlS7dq1XT63HR8fr5MnTyogIEDlypVz3vbt26e9e/dKkn7++We1aNHC5Wv8/bEkNW7c2FnQJalatWouh7Nv27ZNXbp0Ue3atVW+fHndcsstkqSEhASX/TRp0sRlH5Kc+9m+fbuzwF/MpYwtNjZWAwYM0K233qpJkyY5lwMAUFxx4jgAAGymbdu2mj17try8vFS9enWXw7evuuoql3Vzc3NVrVo1rVu3Ls9+Klas6LzvcDhcnsvvQLq/HybucDiUm5srSTp16pSioqIUFRWld955R0FBQUpISNBtt92mM2fOXHA/57/u+f34+fldaNh5XMrYxowZo549e2rlypX67LPPNHr0aC1ZskR33333JX8dAADshJIOAIDNXHXVVapfv/4lrdu8eXMlJSXJ09NTderUyXedhg0basuWLXrooYecywp6crU9e/YoNTVVkyZNUs2aNQu1D+ncLPuaNWvUt2/fi657KWOTpAYNGqhBgwYaMWKE7r//fs2fP5+SDgAotjjcHQCAYuzWW29Vy5Ytddddd2n16tXav3+/Nm/erGeffdZZoocOHaq5c+fqrbfe0q+//qrx48frhx9+yDO7/k9q1aolb29vvfrqq/r999+1YsUKvfDCCwXOO3r0aC1evFijR4/W7t279eOPP2rKlCmFGltmZqaGDBmidevW6cCBA9q0aZO2bt2q0NDQAucCAMAuKOkAABRjDodDq1at0s0336x+/fqpQYMG6tGjh/bv36/g4GBJ586APmrUKD3xxBNq3ry586zsvr6+l/x1goKCtGDBAr333ntq1KiRJk2apKlTpxY47y233KL33ntPK1asUNOmTdWuXTt9++23hRqbh4eHjh49ql69eqlBgwbq1q2boqOjNXbs2ALnAgDALji7OwAApVCHDh1UtWpVvf3221ZHAQAAf8Fn0gEAKOEyMjI0Z84c3XbbbfLw8NDixYv13//+V3FxcVZHAwAAf8NMOgAAJVxmZqY6d+6s77//XllZWWrYsKGeffZZ3XPPPVZHAwAAf0NJBwAAAADAJjhxHAAAAAAANkFJBwAAAADAJijpAAAAAADYBCUdAAAAAACboKQDAAAAAGATlHQAAAAAAGyCkg4AAAAAgE1Q0gEAAAAAsAlKOgAAAAAANvH/FWWRbiQ2IR0AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1200x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,6))\n",
    "# to slant the country in x axis\n",
    "plt.xticks(rotation=75)\n",
    "plt.title(\"Pregnancy vs Columns\")\n",
    "sns.barplot(x=diabetes_df.Pregnancies, y=diabetes_df.Outcome);"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From the chart above, the pregnancy level to outcome isn't uniform although from `14 - 15`are actually diabetic"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.298000</td>\n",
       "      <td>109.980000</td>\n",
       "      <td>68.184000</td>\n",
       "      <td>19.664000</td>\n",
       "      <td>68.792000</td>\n",
       "      <td>30.304200</td>\n",
       "      <td>0.429734</td>\n",
       "      <td>31.190000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.865672</td>\n",
       "      <td>141.257463</td>\n",
       "      <td>70.824627</td>\n",
       "      <td>22.164179</td>\n",
       "      <td>100.335821</td>\n",
       "      <td>35.142537</td>\n",
       "      <td>0.550500</td>\n",
       "      <td>37.067164</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Pregnancies     Glucose  BloodPressure  SkinThickness     Insulin  \\\n",
       "Outcome                                                                      \n",
       "0           3.298000  109.980000      68.184000      19.664000   68.792000   \n",
       "1           4.865672  141.257463      70.824627      22.164179  100.335821   \n",
       "\n",
       "               BMI  DiabetesPedigreeFunction        Age  \n",
       "Outcome                                                  \n",
       "0        30.304200                  0.429734  31.190000  \n",
       "1        35.142537                  0.550500  37.067164  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Checking each mean value \n",
    "diabetes_df.groupby('Outcome').mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* The diabetic people have a greater mean in the `glucose`and `age` column, and the major causes of diabetes is excess glucose in the blood.\n",
    "This and all other factors is what our machine learning model will use in predicting if one has dabeties or not"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Checking Correlation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Pregnancies</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.129459</td>\n",
       "      <td>0.141282</td>\n",
       "      <td>-0.081672</td>\n",
       "      <td>-0.073535</td>\n",
       "      <td>0.017683</td>\n",
       "      <td>-0.033523</td>\n",
       "      <td>0.544341</td>\n",
       "      <td>0.221898</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Glucose</th>\n",
       "      <td>0.129459</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.152590</td>\n",
       "      <td>0.057328</td>\n",
       "      <td>0.331357</td>\n",
       "      <td>0.221071</td>\n",
       "      <td>0.137337</td>\n",
       "      <td>0.263514</td>\n",
       "      <td>0.466581</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BloodPressure</th>\n",
       "      <td>0.141282</td>\n",
       "      <td>0.152590</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.207371</td>\n",
       "      <td>0.088933</td>\n",
       "      <td>0.281805</td>\n",
       "      <td>0.041265</td>\n",
       "      <td>0.239528</td>\n",
       "      <td>0.065068</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SkinThickness</th>\n",
       "      <td>-0.081672</td>\n",
       "      <td>0.057328</td>\n",
       "      <td>0.207371</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.436783</td>\n",
       "      <td>0.392573</td>\n",
       "      <td>0.183928</td>\n",
       "      <td>-0.113970</td>\n",
       "      <td>0.074752</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Insulin</th>\n",
       "      <td>-0.073535</td>\n",
       "      <td>0.331357</td>\n",
       "      <td>0.088933</td>\n",
       "      <td>0.436783</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.197859</td>\n",
       "      <td>0.185071</td>\n",
       "      <td>-0.042163</td>\n",
       "      <td>0.130548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>BMI</th>\n",
       "      <td>0.017683</td>\n",
       "      <td>0.221071</td>\n",
       "      <td>0.281805</td>\n",
       "      <td>0.392573</td>\n",
       "      <td>0.197859</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.140647</td>\n",
       "      <td>0.036242</td>\n",
       "      <td>0.292695</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <td>-0.033523</td>\n",
       "      <td>0.137337</td>\n",
       "      <td>0.041265</td>\n",
       "      <td>0.183928</td>\n",
       "      <td>0.185071</td>\n",
       "      <td>0.140647</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.033561</td>\n",
       "      <td>0.173844</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>0.544341</td>\n",
       "      <td>0.263514</td>\n",
       "      <td>0.239528</td>\n",
       "      <td>-0.113970</td>\n",
       "      <td>-0.042163</td>\n",
       "      <td>0.036242</td>\n",
       "      <td>0.033561</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.238356</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outcome</th>\n",
       "      <td>0.221898</td>\n",
       "      <td>0.466581</td>\n",
       "      <td>0.065068</td>\n",
       "      <td>0.074752</td>\n",
       "      <td>0.130548</td>\n",
       "      <td>0.292695</td>\n",
       "      <td>0.173844</td>\n",
       "      <td>0.238356</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Pregnancies   Glucose  BloodPressure  SkinThickness  \\\n",
       "Pregnancies                  1.000000  0.129459       0.141282      -0.081672   \n",
       "Glucose                      0.129459  1.000000       0.152590       0.057328   \n",
       "BloodPressure                0.141282  0.152590       1.000000       0.207371   \n",
       "SkinThickness               -0.081672  0.057328       0.207371       1.000000   \n",
       "Insulin                     -0.073535  0.331357       0.088933       0.436783   \n",
       "BMI                          0.017683  0.221071       0.281805       0.392573   \n",
       "DiabetesPedigreeFunction    -0.033523  0.137337       0.041265       0.183928   \n",
       "Age                          0.544341  0.263514       0.239528      -0.113970   \n",
       "Outcome                      0.221898  0.466581       0.065068       0.074752   \n",
       "\n",
       "                           Insulin       BMI  DiabetesPedigreeFunction  \\\n",
       "Pregnancies              -0.073535  0.017683                 -0.033523   \n",
       "Glucose                   0.331357  0.221071                  0.137337   \n",
       "BloodPressure             0.088933  0.281805                  0.041265   \n",
       "SkinThickness             0.436783  0.392573                  0.183928   \n",
       "Insulin                   1.000000  0.197859                  0.185071   \n",
       "BMI                       0.197859  1.000000                  0.140647   \n",
       "DiabetesPedigreeFunction  0.185071  0.140647                  1.000000   \n",
       "Age                      -0.042163  0.036242                  0.033561   \n",
       "Outcome                   0.130548  0.292695                  0.173844   \n",
       "\n",
       "                               Age   Outcome  \n",
       "Pregnancies               0.544341  0.221898  \n",
       "Glucose                   0.263514  0.466581  \n",
       "BloodPressure             0.239528  0.065068  \n",
       "SkinThickness            -0.113970  0.074752  \n",
       "Insulin                  -0.042163  0.130548  \n",
       "BMI                       0.036242  0.292695  \n",
       "DiabetesPedigreeFunction  0.033561  0.173844  \n",
       "Age                       1.000000  0.238356  \n",
       "Outcome                   0.238356  1.000000  "
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "diabetes_df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAqsAAAJZCAYAAACOQXzjAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdd1RUx9vA8e8uXXrvHWxYULBE7AV7ib2XqLElRo1G0diisSUaY+899hZ7rNgwKio2sBdUULo0qbvvH6uLC4uC+Av6Op+cPSfMPjP3uetymZ07MyuRy+VyBEEQBEEQBOETJC3uBARBEARBEAQhP6KzKgiCIAiCIHyyRGdVEARBEARB+GSJzqogCIIgCILwyRKdVUEQBEEQBOGTJTqrgiAIgiAIwidLdFYFQRAEQRCET5borAqCIAiCIAifLNFZFQRBEARBED5ZorMqCIKgxrVr1+jTpw+urq7o6upiYGBA5cqVmTVrFnFxccWdnorAwEAkEgmBgYGFrhsaGsqkSZN49OhRnud69+6Ni4tLkfP7EBKJBIlEQu/evdU+/8svvyhj1OX+PkFBQUyaNImEhIRC1XNxcck3J0EQ/jdEZ1UQBCGX5cuX4+Pjw8WLFxk1ahSHDh1i165ddOjQgSVLltC3b9/iTvGjCQ0NZfLkyWo7fOPHj2fXrl3/fVKvGRoasm3bNpKSklTK5XI5a9aswcjI6IPbDgoKYvLkyYXurO7atYvx48d/8HEFQSg80VkVBEF4y7lz5xg0aBANGzbk0qVLDB48mLp169KoUSMCAgK4desWffr0+SjHSk1NVVuenZ1Nenr6RzlGUbi7u1OpUqViO37r1q2Ry+Vs3rxZpfz48eM8fPiQTp06/We5vHr1CoBKlSrh7u7+nx1XEATRWRUEQVAxbdo0JBIJy5YtQ0dHJ8/z2tratGrVSvmzTCZj1qxZlC5dGh0dHaysrOjZsydPnz5VqVe3bl3KlSvHqVOnqFGjBiVKlOCbb77h0aNHSCQSZs2axdSpU3F1dUVHR4cTJ04AEBwcTKtWrTAzM0NXV5dKlSqxdevW955HcHAwnTt3xsXFBT09PVxcXOjSpQuPHz9WxqxZs4YOHToAUK9ePeVt9TVr1gDqpwGkpaUREBCAq6sr2tra2NvbM2TIkDwjlC4uLrRo0YJDhw5RuXJl9PT0KF26NKtWrXpv7m8YGxvz9ddf56mzatUq/Pz8KFmyZJ46R44coXXr1jg4OKCrq4uHhwcDBgwgJiZGGTNp0iRGjRoFgKurq/K830yjeJP7zp07qVSpErq6ukyePFn53NvTAAYOHIiuri6XLl1SlslkMho0aIC1tTWRkZEFPl9BENTTLO4EBEEQPhXZ2dkcP34cHx8fHB0dC1Rn0KBBLFu2jO+++44WLVrw6NEjxo8fT2BgIJcvX8bCwkIZGxkZSffu3fnpp5+YNm0aUmnOeMG8efMoWbIkv//+O0ZGRnh6enLixAmaNGlCtWrVWLJkCcbGxmzevJlOnTqRmpr6zrmTjx49olSpUnTu3BkzMzMiIyNZvHgxVapUITQ0FAsLC5o3b860adMYO3YsCxcupHLlygD5jhzK5XLatGnDsWPHCAgIoFatWly7do2JEydy7tw5zp07p9LBv3r1Kj/++CNjxozB2tqaFStW0LdvXzw8PKhdu3aBXt++ffvSoEEDwsLCKFOmDAkJCezcuZNFixYRGxubJ/7+/ft89dVX9OvXD2NjYx49esScOXOoWbMm169fR0tLi379+hEXF8f8+fPZuXMntra2AJQtW1bZzuXLlwkLC+Pnn3/G1dUVfX19tfnNnTuX8+fP07FjRy5duoSJiQmTJ08mMDCQQ4cOKdsWBKEI5IIgCIJcLpfLnz9/LgfknTt3LlB8WFiYHJAPHjxYpfz8+fNyQD527FhlWZ06deSA/NixYyqxDx8+lANyd3d3eUZGhspzpUuXlleqVEmemZmpUt6iRQu5ra2tPDs7Wy6Xy+UnTpyQA/ITJ07km2tWVpY8OTlZrq+vL//zzz+V5du2bcu3bq9eveTOzs7Knw8dOiQH5LNmzVKJ27JlixyQL1u2TFnm7Ows19XVlT9+/FhZ9urVK7mZmZl8wIAB+eb5BiAfMmSIXCaTyV1dXeUjR46Uy+Vy+cKFC+UGBgbypKQk+W+//SYH5A8fPlTbhkwmk2dmZsofP34sB+R///238rl31XV2dpZraGjIb9++rfa5Xr16qZTdvXtXbmRkJG/Tpo386NGjcqlUKv/555/fe46CIBSMmAYgCILwgd7cqs89wlm1alXKlCnDsWPHVMpNTU2pX7++2rZatWqFlpaW8ud79+5x69YtunXrBkBWVpby0axZMyIjI7l9+3a+uSUnJzN69Gg8PDzQ1NREU1MTAwMDUlJSCAsL+5DT5fjx40De8+3QoQP6+vp5ztfb2xsnJyflz7q6upQsWVJlKsL7vNkRYP369WRlZbFy5Uo6duyIgYGB2vioqCgGDhyIo6MjmpqaaGlp4ezsDFCo865QoYLaaQbqeHh4sHz5cnbv3k2LFi2oVasWkyZNKvCxBEF4NzENQBAE4TULCwtKlCjBw4cPCxT/5ja0ulu9dnZ2eTpl77olnPu5Fy9eADBy5EhGjhypts7b8zBz69q1K8eOHWP8+PFUqVIFIyMjJBIJzZo1Uy4WKqzY2Fg0NTWxtLRUKZdIJNjY2OS5LW9ubp6nDR0dnUIfv0+fPkyePJlp06Zx+fJl5s+frzZOJpPh7+9PREQE48ePp3z58ujr6yOTyahevXqhjlvY2/fNmzfH2tqaFy9eMGLECDQ0NApVXxCE/InOqiAIwmsaGho0aNCAgwcP8vTpUxwcHN4Z/6YzFhkZmSc2IiJCZb4qKDp1+cn93Ju6AQEBtG3bVm2dUqVKqS1/+fIl+/btY+LEiYwZM0ZZnp6eXqQ9Ys3NzcnKyiI6OlqlwyqXy3n+/DlVqlT54LbfxdHRkYYNGzJ58mRKlSpFjRo11MbduHGDq1evsmbNGnr16qUsv3fvXqGP+a5/K3UGDhxIUlISXl5eDB06lFq1amFqalro4wqCkJeYBiAIgvCWgIAA5HI5/fv3JyMjI8/zmZmZ7N27F0B5S3/Dhg0qMRcvXiQsLIwGDRp8cB6lSpXC09OTq1ev4uvrq/ZhaGiotq5EIkEul+fZzWDFihVkZ2erlL2JKcio45vzyX2+O3bsICUlpUjn+z4//vgjLVu2fOcep286mLnPe+nSpXliC3Pe77NixQo2bNjAggUL2LNnDwkJCR9tezNBEMTIqiAIgoqvvvqKxYsXM3jwYHx8fBg0aBBeXl5kZmZy5coVli1bRrly5WjZsiWlSpXi22+/Zf78+UilUpo2barcDcDR0ZHhw4cXKZelS5fStGlTGjduTO/evbG3tycuLo6wsDAuX77Mtm3b1NYzMjKidu3a/Pbbb1hYWODi4sLJkydZuXIlJiYmKrHlypUDYNmyZRgaGqKrq4urq6vaW/iNGjWicePGjB49msTERPz8/JS7AVSqVIkePXoU6Xzfxd/fH39//3fGlC5dGnd3d8aMGYNcLsfMzIy9e/dy5MiRPLHly5cH4M8//6RXr15oaWlRqlSpfD8A5Of69esMHTqUXr16KTuoK1eupH379sydO5dhw4YVqj1BEPISI6uCIAi59O/fn+DgYHx8fJg5cyb+/v60adOGTZs20bVrV5YtW6aMXbx4MTNmzODAgQO0aNGCcePG4e/vT1BQkNoOX2HUq1ePCxcuYGJiwrBhw2jYsCGDBg3i6NGjNGzY8J11N27cSL169fjpp59o27YtwcHBHDlyBGNjY5U4V1dX5s6dy9WrV6lbty5VqlRRjhznJpFI2L17NyNGjGD16tU0a9aM33//nR49enD8+HG1+9L+l7S0tNi7dy8lS5ZkwIABdOnShaioKI4ePZontm7dugQEBLB3715q1qxJlSpVVPZKLYiUlBQ6duyIq6srixYtUpa3a9eOIUOG8NNPP3HhwoUin5cgfOkkcrlcXtxJCIIgCIIgCII6YmRVEARBEARB+GSJzqogCIIgCILwyRKdVUEQBEEQBOGTJTqrgiAIgiAIwjudOnWKli1bYmdnp1xs+T4nT57Ex8cHXV1d3NzcWLJkyQcdW3RWBUEQBEEQhHdKSUmhYsWKLFiwoEDxDx8+pFmzZtSqVYsrV64wduxYhg4dyo4dOwp9bLEbgCAIgiAIglBgEomEXbt20aZNm3xjRo8ezZ49ewgLC1OWDRw4kKtXr3Lu3LlCHU+MrAqCIAiCIHyB0tPTSUxMVHmkp6d/lLbPnTuX54s8GjduTHBwMJmZmYVqS3yDlSC8x0CJUXGnUCiLzq4t7hQKRZ6dVdwpFIpGhTrFnULhfIY3z+SJMcWdQuHo6hd3BoWS3LNDcadQKCX6dinuFApFo8OI//kxPtbfJZuJI5g8ebJK2cSJE5k0aVKR237+/DnW1tYqZdbW1mRlZRETE4OtrW2B2xKdVUEQBEEQhC9QQEAAI0aodq4/5jfRSSQSlZ/fzDzNXf4+orMqCIIgCILwGflYczh1dHT+Z1+TbGNjw/Pnz1XKoqKi0NTULPRXUYvOqiAIgiAIwmdEWsiRyeLw1VdfsXfvXpWyw4cP4+vri5aWVqHaEgusBEEQBEEQhHdKTk4mJCSEkJAQQLE1VUhICOHh4YBiSkHPnj2V8QMHDuTx48eMGDGCsLAwVq1axcqVKxk5cmShjy1GVgVBEARBED4jxTHSGBwcTL169ZQ/v5nr2qtXL9asWUNkZKSy4wrg6urKgQMHGD58OAsXLsTOzo558+bRrl27Qh9bdFYFQRAEQRA+I9JimAVQt25d3rU1/5o1a/KU1alTh8uXLxf52GIagCAIgiAIgvDJEiOrgiAIgiAIn5EvbaRRdFYFQRAEQRA+I5/DbgAfk+isCoIgCIIgfEa+tJHVL+18BUEQBEEQhM+IGFkVBEEQBEH4jBTHbgDFSXRWBUEQBEEQPiNf2m3xL+18hc+ci4sLc+fOLe40BEEQBEH4j4iR1c9M7969Wbt2LQCampo4OjrStm1bJk+ejL6+fjFn97938eLFz/o8PWrVwH/UDzj5eGNiZ8viNl24+vf+Ysll4/FzrDp4iuiEJDzsrQno2gLfkq5qY6MSEpm1eT83Hz/j8YtYujeswdiuLVViDgffYNn+E4S/iCUrOxtnawt6N6lF6xqVP0q+m06cZ9U/p4lOSMbDzooxnZvhW9JFbWx0QhKzth7k5uMIHkfF0r1BdQI6N8+37QMXrjFy2Vbqe5dhwXfdPig/uVzOguWr2bJ7D4lJSVT0KsuEUSPwdFf/mr7xz/FA/ly6gvCnETg52DF84Lc0qldb+XxWVhbzl69m76EjxMTFYmluztctmjL4m15IpVIys7KYu3g5p4L+5cmzCAwM9KlRxZcfvxuItaXFu/NdsZotu/e+le9wPN0Kku9Kwp9F4GRvx/BB/WlUNyff+m068izyeZ56Xdu1YeJPI/KUT5j+G1t27yVg2Hf07tIx3+Nu3HOQldv+Jjo2Hg8XR8YO+gbf8mXzjb9w9SYzlq7m3qMnWJmb0a9jGzq3bKx8/u6jcOat3czNu/eJeBFNwKA+9Gqr+p7Oys5mwbot7D1+ipi4BCzNTPnavx6DurVHKn33WI9cLmfB6g1s3XOAxKRkKpQtzYQRQ/B0dXlnvX8CTzNvxTrCIyJxsrNl2Le9aVTbT/n8pl172bR7P8+evwDAw9WZIb27Ubt6FbXtTfjtT7buOUDA9wPo1bHtO4/9Nq0W7dFu3x2JmQWyxw9IXzKH7JshamM1KlSmxKylecpT+rVH9vRxnnLNOo3QC5hGZlAgab+MKnBO77Lp/E1Wnb5KdHIqHlamjGlWA18XW7WxR24+YPOFUG5FxpKRnY2HlSlD6vtS09NRGbPtYhh/h9zh3os4AMraWTLMvyoVHKw+Sr5FJfnCdgMQI6ufoSZNmhAZGcmDBw+YOnUqixYtUvtdu5mZmcWQ3f+WpaUlJUqUKO40PpiOvj5Pr95g83eF/27kj+nA+avM2LiPAS3qsXPyUHxKujBgzmoiYhPUxmdmZWFmqM+AFvUo7WijNsbEQI8BLeqx6efB7J4yjK9r+jBu5XbOXL9T5HwPXrjO9M0HGNCsLjsmDManpDMD/lyXb74ZWVmYGuozoHkdSjmoz/eNZ7Hx/LbtED6ezkXKcfm6jazetIUJo4azfc1yLMzN6PP9cJJTUvOtc+XaDYaPm0Trpo35+6/VtG7amGFjJ3D1xk2Vdjfv/JsJo4ZxYMsGRn0/iJUbNrF+6w4A0tLSCL19h0Hf9GLn+pUsmPkrj548YdCPY96d7/qNrN64lQkjh7F99TIszMzo8/2Id+d7/QbDf56syHfDqtf5TuTqjVBlzPbVyzhzYJfysXr+HACaNKiXp72jJ09z9WYYVu/oVAMcCDzD9MWrGdilHbsWz8a3XBm+HTuViKhotfFPI18w4Oep+JYrw67FsxnQpS2/LlrJP6fPKWPS0tNxtLXmx749sDQzUdvOis272LzvH8Z/14/9K+cxsn8PVm7bzYbdB96ZL8CKjVtZs2Un44cPYdvy+ViamfLN8ACSU9/x+t4IZcSkabRq3IC/Vy+iVeMGDJ/wK1dv3lLGWFtZ8uPAb9i+fD7bl8+neuWKDAmYxN2Hj/K0d/RUENdCb2FlYf7efN+mWbsROgNGkLF5NalDupN9IwS9qX8isbR+Z73kvu1I7tJE+ZBFPMkTI7GyQaffD2RdL/q3Gr1x8Po9ph8IYkDdSuwY3A4fZxsGrDtAREKS2vjgR5HU8HBgSc+mbBvUjqqudgzecIjQiBhlzIWHETSv4MHqvi3ZOKANtiYG9F+znxeJKR8t76KQfqTH5+JzylV4TUdHBxsbGxwdHenatSvdunVj9+7dTJo0CW9vb1atWoWbmxs6OjrI5XJevnzJt99+i5WVFUZGRtSvX5+rV6+qtDl16lSsrKwwNDSkX79+jBkzBm9vb+XzvXv3pk2bNvz+++/Y2tpibm7OkCFDVDrEGzZswNfXF0NDQ2xsbOjatStRUVHK5wMDA5FIJBw7dgxfX19KlChBjRo1uH37tkoue/bswdfXF11dXSwsLGjbNmc0IPc0gPed29WrV6lXrx6GhoYYGRnh4+NDcHBwUf8JPtjNQ0fYM34KIbv2FlsOAGsPn6FtbV861KmKu50VY7u2xMbMmM3H/1Ubb29hxthurWjj54OBnq7amKql3WnkUw53OyucrMzp6V+Tkg42XLr7qMj5rjlylnY1fWhf2xd3OysCOjfH1tSYzYEX8snXlLFdmtO6RiUM9XTybTdbJmP08m1816o+jpZmH5yfXC5n3eatDOzdE/96dSjp7sbMieNIS0tn3z9H8q23dvM2alT1ZUDvHri7ODOgdw+qV/Fh7eZtypiQ6zdoULsmdWvWwMHOliYN6lGzWlVuhCk6MIYGBqxe8AfNGtXHzdkJ7/Je/DxyGDdv3Sbi9eib+ny3MbBPj7fyHVuIfLu/zrd7nnzNTE2wNDdXPk6cCcLJwZ6qlb1V2noRFc0vv83l91/Go6X57pt8a3bspV2TBnRo1gh3ZwfGDu6LjaU5m/b+ozZ+875/sLW0YOzgvrg7O9ChWSPaNq7Pqm1/K2PKl/Lkp2970bxeTbS0tNS2cyXsNg1qVKVuNV8cbKxoUrsGfj7e3Lhz/535yuVy1m3dzcCenfGvU5OSbi7MGDeStPR09h05kW+9ddt2UcO3MgN6dMbN2YkBPTpT3cebtdt2KWPq+1WnzldVcXVywNXJgeHf9qGEnq5KhxbgRXQMU+Yu5LcJo9F8z+ubm3bbrmT+8zeZh/5G9uQR6UvnIIt+gVaL9u8+74Q45PGxygcymWqAVIru6ClkbFiG/HlEoXJ6lzVnr9POpzTtfcvgbmVKQHM/bI0N2HwhVG18QHM/+tbypryDFS4Wxgz3r4azuTGBt3JGgX/r2IAu1bwoY2uBm6Upv7SpjUwu59/7zz5a3kLBic7q/wN6enrKTuO9e/fYunUrO3bsICQkBIDmzZvz/PlzDhw4wKVLl6hcuTINGjQgLk5xe+Ovv/7i119/ZebMmVy6dAknJycWL16c5zgnTpzg/v37nDhxgrVr17JmzRqV7wLOyMhgypQpXL16ld27d/Pw4UN69+6dp51x48Yxe/ZsgoOD0dTU5JtvvlE+t3//ftq2bUvz5s25cuWKsmOrjlwuf++5devWDQcHBy5evMilS5cYM2ZMvn+YvhQZWVncfPQMPy9PlXI/L0+u3M97y+5DyOVyzoXe49HzaHxLvfu28vtkZGUR+jgCPy8PlfIaXh6E3A8vUtuL9p7A1FCfdrXUv8cK6mlEJNGxcdR861astrY2VSp7c+XajXzrhVy/Qc1qqrdva1WvqlLHx7sC/wZf4uFjxbneunOPS1evUafGV/m2m5ycgkQiwcjA4N35VsuVb6WKXLn+rnxvqs83nzoZmZnsOXSEdi2bqdy2lMlkjJo0lb7dO7932kFGZiY379zHz6eiSrmfjzdXcnXQlHmG3cHPx1ulrKavNzfv3CczK+udx3ubT7kynLtyjYdPFR2rW/cfcvlGGLWrvntqy9PI50THxeFXxUdZpq2tTRXv8ly5ob4DBRByI0ylDkDNqr6E5FMnOzub/UcDSU1Lx9urjLJcJpPx09RZ9O3S/r3TDvLQ1ETqWZrsy+dVj3X5PBplKryzqv7CDehvPIje9EVoVPDJ87x2137IE+LJ/GdP4XJ6h4ysbEIjovHzcFApr+HhQEi4+g9ruclkclLSMzEukf8H27TMLLKyZRi/48Pvf0kq+TiPz4WYs/qZu3DhAhs3bqRBgwaAosO4fv16LC0tATh+/DjXr18nKioKHR3FL9nvv//O7t272b59O99++y3z58+nb9++9OnTB4AJEyZw+PBhkpOTVY5lamrKggUL0NDQoHTp0jRv3pxjx47Rv39/AJVOp5ubG/PmzaNq1aokJydj8NYfzV9//ZU6deoAMGbMGJo3b05aWhq6urr8+uuvdO7cmcmTJyvjK1ZU/SP1xokTJ957buHh4YwaNYrSpUsD4OnpqbatL0lCUirZMhkWRoYq5ebGhsTcKNot+6TUNOqOmEZGVhZSiZQJPVrn6RQXVkKyIl9zI9WOl7mRPjEvk/Op9X6X7z5m55lL7JwwpEj5AUTHxipyMlMdnbUwMyVCzfzNN2Ji4/LUMTczIzo2Tvlz/57dSEpOpmnH7mhIpWTLZAwf1J8WjRuqbTM9PZ3fFyyhReOGGBjog1xeiHzNiHj+vnxNc+VrqpLv246ePE1ScjJfN2+qUr583UY0NTTo2endI3UA8S+TFP/+piaqxzU1JiY+QW2d6Lh4avp654o3ISs7m/iXiViZF2wUvX+nr0lKSaXZN98rX/thfbrSon6td9Z783rkea1MTYl4HqWuCgAxcfGY55qSYG5mQnRcvErZ7fsP6TJoGOkZGZTQ02PBrxPwcM2ZxrL8r61oaGjQo32bApylKomRCRINTWTxqv+m8vhYpGbqpxPI4mJJm/sr2ffCQEsbrfrN0JuxiFc/DST7xhUANMpWQKtxK1KHfNic8PwkpKaRLZNjbqCnUm6ur0dMcv5TLt62+uxVXmVk0qSce74xcw6fx8pIn6/c7YuU78fypY00is7qZ2jfvn0YGBiQlZVFZmYmrVu3Zv78+SxatAhnZ2dlRxXg0qVLJCcnY26uepF59eoV9+8rbmXdvn2bwYMHqzxftWpVjh8/rlLm5eWFhoaG8mdbW1uuX7+u/PnKlStMmjSJkJAQ4uLikL2+BRQeHk7ZsjkLISpUqKDSBkBUVBROTk6EhIQoO7/vU5BzGzFiBP369WP9+vU0bNiQDh064O6e/wUpPT2d9PR0lbJs5GjwGX0ELahcpySXy5EU8Tz1dbXZOXkoqekZ/Bt6j5mb9+NoZUbV0vm/5gWVez2BXJ63rKBS0tIZvXIbk3u2wdSw8Av29hw6zMTpvyt/XvrHzHxyfH+SuRdKyJGrlB04cow9B48we8oEPNxcCbtzl+lz5mNlYcHXLVQ7gZlZWQwfNwm5XMakn35UzXfG7Jx85+STLwXIN9d7RC6X57vYY8ee/dT+qprKQq8bYbdZt2U7O9etKNQikTyx8ncvMskbL1df/g4HAs+y99hJfg8YjoeLI7fuPWTa4lVYmZvxtX/OHNy9h48z8fc/lT8vmTlFcazcDcrl733Pqj9P1SJXJwd2rVpEYnIKhwPPMObX31k//zc8XJ25cfsu67fvZsfKhUVchJPrQ45Eong/q4t8+pjMtxZSpYddR2ppjXb77ry6cQX0SqD70y+k/TkNeeLLIuSUv9xnKifve1Wd/Vfvsej4JeZ3a5ynw/vGytMh7L92n7V9W6KjJbpNxUG86p+hevXqsXjxYrS0tLCzs1O5rZ17pbxMJsPW1pbAwMA87ZiYmCj/P88fTDUXpdy3zyUSibJDmpKSgr+/P/7+/mzYsAFLS0vCw8Np3LgxGRkZ+bbz5rhv2tHTU3+xUKcg5zZp0iS6du3K/v37OXjwIBMnTmTz5s18/fXXatucPn26yqgugA/a+PJp3Pr5GEwMS6AhlRLzUnXxQVxiMubG6m8bF5RUKsXZWtExKeNkx/2IKJbtCyxSZ9XE4E2+qqOocUkpeUZbCyo8Ko5nMQkMmb9BWSZ7/Z4v/+0E9k/9ASer/Bel1K9Vk4peOR/AMjIU03BiYuOwssjpmMXGJ2Bhlv8onoW5GTGvRznfiIuLx+KtEblZ8xbzba9uNPdXjKSW8nAnIvIFS9duUOmsZmZlMSxgAk8jIlm76E/FqGp++Wbmk2+uY6vNN051xC0uPkFtnWeRzwm6eIn5M6aolAeHXCU2Pp56rTsoy7Kzs5k5bxHrtmzn+O6tKvGmxoaKf/9co4uxCS8xNzFWm6elmSkxcQl54jU1NDDJdUfhXX5bvpb+ndrSvF5NAEq5OhMRFc2yzTtVOqv1alanQtlSyp+Vr29cvMriptiEhDyjrW+zMDMlJjbXecYnYGGqWkdbSwtnB8UIX/nSJblx6zbrtu/ml1E/cOnqdWLjE6jfvrsyPjtbxsyFy1m7bTfHt6175znLExOQZ2chNTXn7RmnEhMz5PHqR9DVyb51Hc36iven1NYBqY09epNzPjAhUYwNGuw/R0q/9sgjP2wuqEkJXTSkEmKSX6mUx6W8yrfz+cbB6/cYv/skf3RuSI1c0wjeWHXmKstOXmFlnxaUsincQrX/JekXthuA6Kx+hvT19fHw8Hh/IFC5cmWeP3+OpqYmLi4uamNKlSrFhQsX6NGjh7KssIuQbt26RUxMDDNmzMDR0fGD2gDFqOuxY8eUUxLepSDnBlCyZElKlizJ8OHD6dKlC6tXr863sxoQEMCIEarb6/xo/Gnc9vlYtDU18XKxJ+jmPRr5lFOWB4Xeo753/lsBfQg5ijmnRaGtqUlZZzuCQu/RsHJOfop8y7yjZv7cbC34e/L3KmV/7jpKSlo6Y7s0x8ZMfSfoDQP9Ehjo5+xKIZfLsTQ34+z5i5QtVRJQdFguXg5h5HcD823Hu3w5zl4IpnfXTsqyM+cvUqlCzr9LWlpang+TGhpS5G8tXnnTUX385CnrFv+Jaa5OXL75XghWzffKVUYOGfCOfL04e/6iyhZTZ85fpFL5cnlid+47gLmpCXX9VOfWtm7WmBpVVecI9/1hJK2b+tO2RbM87WhraeFV0p2gy1dpVLO6sjzo8lXq16iqPs8yJTnxr+r15+ylq3iVdH/vYq63vUpLR5prYp9UKlV+uH7DoEQJDErken3NzAi6eJmyJRXX6ozMTC6GXOfHgX3zPZ53uTIEBV+md6ecRaVnL17Cu9y7fy/l8pwPTK0aN+QrX9U5tf1+HEvrxg34upn/O9sBICsL2d1baFSqRlZQoLJYo1JVsv499f76r0ndSyGPU6yulz15RMqAzirPa/caiERPn/Qls5FHF2xuqTramhqUtbMk6N5TGpbNmf8cdO8p9cu45Ftv/9V7/LwrkN86NqBOKfU7gaw8HcLSwCss792McvaWamOKi5gGIPy/0rBhQ7766ivatGnDzJkzKVWqFBERERw4cIA2bdrg6+vL999/T//+/fH19aVGjRps2bKFa9eu4ebmVuDjODk5oa2tzfz58xk4cCA3btxgypQp76+Yy8SJE2nQoAHu7u507tyZrKwsDh48yE8//VToc/Py8mLUqFG0b98eV1dXnj59ysWLF2nXrl2+x9fR0VHOf33jY04B0NHXx9Ij53W1cHXBoWJ5UuLiiX/y9KMd5316+ddkzPKtlHOxx9vDma0nzxMZm0CnetUAmLPtEC8SXjKzf04nKixcscgkNT2D+KQUwsIj0NLQwMNesZ3Nsn0n8HJ1wMnSjMzsbE5du82eoMtM6NGmyPn2buTH6JXb8XKxx9vNkW2ngomMe0mnuorFPnN2HCYqIZEZfXPmQIaFRyrzjUtKISw8Ei1NDTzsrNDR0sLTXnUbHqMSil0OcpcXhEQioWfnjixdswEXR0ecnRxYuno9uro6tGjcSBn308SpWFtZ8OMQRQe2Z+f2dB/wPcvW/kWDOjU5dvIM5y4Es3H5QmWderVqsGTNeuxsrBXTAG7fZfXGLbRrqdg3Nisri6FjxhN66w5L58wkO1tGdIxitNbY2AhtNZ0zRb4dXufrgLOjA0vXbMib76Rfsba04MfXHdiendrTfeBQlq37iwa1a3Ls1Ot8ly1UaV8mk7Fz30HaNG+SZyW6qbExpsaqnWktTU0szMxwc3ZS+/r2bteS0TPnUa6kB95lSrH1wGEio2Lo3ELR+Zq9cgNRMbHMHP0DAJ1bNOavPQeZvmQ1HZs2IiTsNjsOHeP3scOVbWZkZnL/seJ3LjMzixcxcYTde0gJPV2c7RXTk+pVr8KSjduxtbLAw9mJsHsPFDsTNK6vNk+V17djG5Zu2Iyzoz3ODvYsXb8JXR0dWjTKGZEdPXUWVhYW/DhQMd+/R/s29Ph+JMv/2kKDml9x7Mw5zgVf4a+Fc5R15ixdRe3qVbCxsiQl9RUHjgVyIeQay3+f+vr1NcLU2EglH01NTSzMTHFzcqQgMnZuRHfUZLLvhiILu45W06+RWtmQuV+xXZp2nyFIzS1J+30SAFptuiB/EUH24wdItLTQrN8UrVoNeDXl9XU7MwPZ41w7KKQkI4e85R+gt195Rm8/gZe9Jd6O1mwLDiPyZTKdqig6+XMOnycqMYUZ7RX/bvuv3iNgxwkCmtegoqM10UmKua26WhoY6iqu/ytPhzDv6EV+69gAOxNDZUwJbS30dYp/ke7ntDjqYxCd1f/nJBIJBw4cYNy4cXzzzTdER0djY2ND7dq1sbZW/FHu1q0bDx48YOTIkaSlpdGxY0d69+7NhQvqtwVSx9LSkjVr1jB27FjmzZtH5cqV+f3332nVqlWh8q1bty7btm1jypQpzJgxAyMjI2rXrq029n3npqGhQWxsLD179uTFixfKbbBy3+b/Lzn7VmJEYM4ejR3+mA7AuTV/sbbPoP8sj2bVKpKQksqiPceIfpmEp70NS4b3xt5Ccbsx+mUikbn2MG07cZ7y/28+esa+f0OwMzfh2O+K/TxT0zP4Zd1uXsS/RFdbC1cbS2b270SzauoXyBVG06rlSUhJZfHeE4p87axZ+kMP7M0V+ca8TMqTb7tfcjpQNx9HsP/8NezMTTg683+zx23/nl1JT09n8qzZvExKpqJXGVbNn6Myohn54oXKSF3lCuWZM3Uic5esYN7SFTg62PPHtMlULOeljPl55HD+XLqCybPmEBsfj5WFBZ2+bs2Qfr0BeB4VzfFTZwBo3V31jsS6xfOolmvLKGW+Pd7kOycn33mz35/vlInMXbqCeUtX4uhgxx+/TqJirpG/oAvBRDx/oexQF1WzujVJSExi4YatRMfF4+nixNJfx2FvrdigPTo2noionD0yHWytWTr1Z2YsWcXGPQexMjdj3OC+NK6VM8obFRvP14Ny5vWu2vY3q7b9TZUKXqyfrfig/fN3/Zi3ZiO/zFtGbEIiVuamdGruz+DuOVMY8tOva0fS0jP4ZfYCXiYnUaFMaVbOma4yAhvxIhqJJGeMrHJ5L2ZPHMufK9Ywb8U6HO1tmTN5LBW9SitjYuMT+Gnqb0THxmGoX4JS7q4s/31qnl0EiiLr1BHSjYzR6dYPiakFssf3eTV+GPIoxeI7qZkFEquc/Yslmppo9/8BibklZKST/fgBqeN/IPti0EfL6V2alvcgITWdxScuEZ2Uiqe1GUt7NMXeVDHlIyYplciEnGlEWy+GkiWTMWXvGabsPaMsb1OpJNPaKT5MbDp/k8xsGcM2qW7lNrieD981KNruIULhSeT5zZgWvmiNGjXCxsaG9evXF3cqxW6gxOj9QZ+QRWfXFncKhSLPLto0gf+aRoU6xZ1C4XyGl3h5Ysz7gz4lup/Xt+ol93x/Z/tTUqJvl+JOoVA0OuT9praPbabeh+8L/bbRrwo+D7k4iZFVgdTUVJYsWULjxo3R0NBg06ZNHD16lCNH8t8cXBAEQRCE4iH9/7hDzTuIzqqgvJ0+depU0tPTKVWqFDt27KBhQ/X7OAqCIAiCIPxXRGdVQE9Pj6NHjxZ3GoIgCIIgFIBYYCUIgiAIgiB8sr60rau+tPMVBEEQBEEQPiNiZFUQBEEQBOEzIqYBCIIgCIIgCJ+sL203ADENQBAEQRAEQfhkiZFVQRAEQRCEz4iYBiAIgiAIgiB8sr602+KisyoIgiAIgvAZ+dJGVr+0zrkgCIIgCILwGREjq4IgCIIgCJ+RL203ANFZFQRBEARB+IyIaQCCIAiCIAiC8IkQI6uC8B6Lzq4t7hQKZbBfr+JOoVAWHl9S3CkUivz5g+JOoVBke9YXdwqF5+pZ3BkUjo1DcWdQKCU6tSjuFAol+9Ch4k6hUDQ6jPifH+MLG1gVnVVBEARBEITPiZgGIAiCIAiCIAifCDGyKgiCIAiC8BkRuwEIgiAIgiAInywxDUAQBEEQBEEQPhFiZFUQBEEQBOEz8qWNNIrOqiAIgiAIwmfkC5sFIDqrgiAIgiAInxOp5Mvqrn5pI8mCIAiCIAjCZ0SMrAqCIAiCIHxGvqxxVdFZFQRBEARB+Kx8aZ1VMQ1AEARBEARB+GSJkVVBEARBEITPiBhZFYQikEgk7N69u7jTEARBEIT/tyQSyUd5fC7EyKpQYM+fP2f69Ons37+fp0+fYmxsjKenJ927d6dnz56UKFGiuFMsVhuPn2PVwVNEJyThYW9NQNcW+JZ0VRsblZDIrM37ufn4GY9fxNK9YQ3Gdm2pEnM4+AbL9p8g/EUsWdnZOFtb0LtJLVrXqPxfnA4AHrVq4D/qB5x8vDGxs2Vxmy5c/Xv/f3b8t20KvMiqI0FEv0zCw86KMR0a4+vprDY2+mUSs7Yf5mZ4JI+jYulerxoBHZuoxOwKCmHcur/z1L0yfxw6WoW7NG48cIyVOw8QHf8SDyc7xvbrhq9XqXzjL9y4xYyVG7kXHoGVmQn92jajc9P6yud3HjvN2D9X5Kl3dftydLS1Aajf70ciomLyxHRt1oAJA3sWKn8AiXctJFUagoExxEQiO74dnt1XH2zvjrROazCzBk1tSIxDfvUM8ksncmI8KyKt3hhMLEGqAQnRyC8eQx56odC5qbPp3xusOhNCdFIqHlamjGnuh6+LndrYIzcfsPn8TW5FxpCRnY2HlRlDGvhS09NJGbPtYih/X7nNvRdxAJS1t2RYo2pUcLT+OPke/5dV/5x5fX2wYkzn5viWdFEbG52QyKytB7n5KELx/m3wFQFdmufb9oHz1xi5bAv1vcuw4PvuHyffy3dYdT6M6ORXeFgYM6ahD76OVmpjj9x+wuYrd7n1Il7x+loYM6RmeWq6qf57JKZl8Oepqxy5/YTEtAwcTAwYVb8Sddzti5yvtF5LNBp3ABMz5M8ek715MfK7N95bT+JRFs2fZiN/9oisyYOU5ZqjfkNaumKeeNm182T9Ob7I+QqFIzqrQoE8ePAAPz8/TExMmDZtGuXLlycrK4s7d+6watUq7OzsaNWqVXGnWWwOnL/KjI37GN+jNZU9XdgSeJ4Bc1az99cR2Jmb5InPzMrCzFCfAS3qse7wGbVtmhjoMaBFPdxsrdDS1CAwJIxxK7djbmhAzfIl/8dnpKCjr8/TqzcIWr2BgTv/+k+Oqc7B4BtM33aICV2aU8ndka2nLzFgwV/snTgEOzPjPPEZmdmYGpRgQNNarD32b77tGujqsH/ydyplhe2oHjh9nukr/mLCwJ5ULlOSLYdO8O3k2exbOB07S/M88U+fRzNg8mw6+NfltxEDuRx2h1+WrMPU2JDGNark5FZCj4OLZ6jm9rqjCrB99kSyZTLlz3cfP+ObCbNo7FeFwpKUqoykfnvkR7Ygf3YfScWaSNsPQbZqCiTF562QmY788knk0RGQmY7EwR1Joy6QmYH82llFTFoqsn//gdjnIMtG4lYOSdPuyFOT4FFYoXN828Fr95h+4CwTWtaikrMtWy/eZMDa/ez9oTN2JoZ54oMfRVDDw4Fh/tUw1NVm1+VbDF5/kM0D21LWzhKACw8jaF7BE28nG3S0NFh5KoT+a/axZ2gnrI0NipbvhWtM33yACd1bUsnDma0nLzJg7lr2TvlB7fUhIysbUwN9BrSoy9rDZ9/Z9rOYeH7bdhAfT5ci5aiSb9hjph+9zITGvlSyt2RryD0GbA1kb7/m2Bnr54kPfhJFDRcbhtWpiKGOFruuP2Dw9lNs7ulPWRszxTllZ9Nv83HM9HWZ+3UtrA1L8DwxBX1trSLnK61SB43OA8neMB/ZvZto1GmO5rBfyRzfD+Ki86+oVwLNvj8hD7sCRqYqT2Ut+gU0cq4FEgMjNCctQRZ8qsj5fgyfz5joxyGmAQgFMnjwYDQ1NQkODqZjx46UKVOG8uXL065dO/bv30/Lli3z1AkMDEQikZCQkKAsCwkJQSKR8OjRI2XZ2bNnqVOnDiVKlMDU1JTGjRsTH6/4A5mens7QoUOxsrJCV1eXmjVrcvHiRWXd+Ph4unXrhqWlJXp6enh6erJ69Wrl88+ePaNTp06Ymppibm5O69atVY79saw9fIa2tX3pUKcq7nZWjO3aEhszYzYfV99RsrcwY2y3VrTx88FAT1dtTNXS7jTyKYe7nRVOVub09K9JSQcbLt39+Pnn5+ahI+wZP4WQXXv/s2Oqs+bov7Tzq0T7mpVxt7UkoGMTbE2N2Xzyotp4ewsTxnZqSuvqFTHU1cm3XYkELI0NVB6Fzu3vQ7RrWJsO/nVxd7RjbP9u2FiYsenAMbXxmw8dx9bSnLH9u+HuaEcH/7q0bVibVbsO5spNgqWpicrjbWbGRirPBV4MwcnGiqrlShf6HCS+DZBfP4f8ehDEvUB+YgckxSPxrqW+QtRT5LcuQWykYlQ19KKiA+rgkRPz5C7cvQpxLyAhBvnlQIh+hsTevdD55bbm7FXa+ZSmfZWyuFuZEtC8JrbGBmw+f1NtfEDzmvStXYnyDla4WJgw3L86zubGBN56rIz5rWNDulQvRxk7C9wsTfnl6zrI5HL+ffCs6PkePku7Wj60r10FdzsrAro0x9bMmM2B59XG21uYMrZrC1rXqIRhCfXXB4BsmYzRy7fxXesGOFqa5htX6Hwv3KJdRTfaV/TA3cKYgIY+2BqVYPOVu2rjAxr60Ld6WcrbmuNiZsTwOt44mxkSeC/ntdt57QEv0zKY37Y2lR0ssTfWx8fRitLWRc9b6t8O2elDyE4fgsgnZG9eAnHRaNTN+3fpbRo9hyE7fwL5fTUfnlKSIDFe+ZCUrQwZacguni5yvh+D9CM9PhefU65CMYmNjeXw4cMMGTIEff28n6qBD577EhISQoMGDfDy8uLcuXOcOXOGli1bkp2dDcBPP/3Ejh07WLt2LZcvX8bDw4PGjRsTF6e4VTd+/HhCQ0M5ePAgYWFhLF68GAsLCwBSU1OpV68eBgYGnDp1ijNnzmBgYECTJk3IyMj4oHzVycjK4uajZ/h5eaqU+3l5cuX+43xqFY5cLudc6D0ePY/Gt5T6qQX/X2VkZRMaHoFfGdVOTo0yboQ8eFqktlPTM2gwdi71xsxh0MKNhIZHFi63zCxu3nuEX6VyKuV+lcpx5dY9tXVCbt3LE1+zUjlu3ntEZlZWTm6v0qjfdwR1+gxjwC9zCH3HeykjM4s9gUG0bVi78L+LUg2wcUSea7RT/igMib1bwdqwcgB7N0UHNT9OpcDUGvlT9a9LQWVkZRMaEY2fh6NKeQ0PR0LCnxeoDZlMTkp6JsZ6+X+QScvMIitb9s6YguWbRejjCPy8PFTKa5T1IOReeJHaXrTnOKaGJWhXy7dI7bwtIzub0Odx+LnYqpTXcLEh5FneaSfqyORyUjIyMdbLuRNw4u5TKtpbMPXwRWrN20mrFftZGnRT5e7AB9HQROLsiezmZdUcQi8h8SibbzWpnz8SS1uy96wv0GGktZogu3ASMtKKlO7HIpF8nMfnQkwDEN7r3r17yOVySpVSnYNnYWFBWpriF3fIkCHMnDmz0G3PmjULX19fFi1apCzz8vICICUlhcWLF7NmzRqaNm0KwPLlyzly5AgrV65k1KhRhIeHU6lSJXx9FRdrFxcXZTubN29GKpWyYsUK5R/w1atXY2JiQmBgIP7+/oXOV52EpFSyZTIsjFRvP5obGxJz406R2k5KTaPuiGlkZGUhlUiZ0KN1nk7x/3cJyalky+SYG6mOepobGRCTmM+cygJws7Hg115tKGlvRfKrdDYcP0/331ax8+eBuFjnvX2vTnxiEtkyGeYmqlMRzI2NiUl4qbZOdMJLahrnijcxJis7m/jEZKzMTHCzt2X6D/0o6eJIcuor1u09TNfRU9k9bwoudjZ52jx2/hJJKal83aBmAc/+LXoGSKQakJKoWp6SBPpG76wqHTgV9AxAqoE8aL9iZPZt2rpIB01T3E6Vy5Af2QKPbxU+x7ckpKYp3g8GqnPkzQ30iElOLVAbq8+G8Cojkybl8x/lnfPPv1gZ6fOVu0PR8n19fcjz/jU2IOZG8ge3e/nuY3aeucTOid+9P7gQElLTyZbLMddXHdE119cjJqVgH+ZWXwjjVUYWTUrnzCl/mpDC+ccvaOHlwpKOdXkcl8iUw8Fky2QMrln+wxM2NEKioaEYAX2L/GU80nL5jNpa2aHRri+ZM0dAATrLEtdSSB1cyVwz58PzFIpEdFaFAss9YnPhwgVkMhndunUjPT39g9oMCQmhQ4cOap+7f/8+mZmZ+Pn5Kcu0tLSoWrUqYWGKUaBBgwbRrl07Ll++jL+/P23atKFGjRoAXLp0iXv37mFoqNqJTEtL4/599Z2c9PT0POeilZGJTkHmVeX6lCqXy5EUcWaRvq42OycPJTU9g39D7zFz834crcyoWrrot1I/N7lHARSv74er6OZARbecjkhldyfaTVvKX4EXGNepaSFzy53Ju//t84bLVcq9S3vgXTpnJK5yGU/aDp/Ihn1H+fnbvAtoth85RS2fClibf7xbwUhy8sqPbNMfoKWDxM4FSe3WEB+tmB7wRkY6srXTQVsHiVMpJPXaIn8Z8+4R2IKml+f9QIF+3/ZfvcuiY8HM7940T4f3jZWnrrD/2j3W9mtd6DnM+cmdm1wu/+CRrZRX6YxesY3Jvdpgaqj+bldR5Xl93/OefmN/6CMWnbnO/HZ1VDq8MrkcM31dJjepioZUipeNGVHJr1h1PqxondW3MsxzAurevhIpmt8GkP33OnhRsCke0ppNkD19iPzh7aKn+ZEU9W/L50ZMAxDey8PDA4lEwq1bqiMibm5ueHh4oKenp7aeVKp4e8nf+oOXmZmpEpNf3bfr5e4IKC7yirKmTZvy+PFjhg0bRkREBA0aNGDkyJEAyGQyfHx8CAkJUXncuXOHrl27qj3m9OnTMTY2VnnMWL8j3xwBTAxLoCGVEvMySaU8LjEZ8yIuzJBKpThbW1DGyY4+TWrj71uOZfsCi9Tm58bEoAQaUgkxL1VHoeKSUvKMVhWFVCqhvLMdj6PiClzH1MhQ8W8fn6BSHvsyEXMT9aOSliZ5R11jXyaiqaGBiaH685FKpZT3dOVxRN7b3M+iYjh39SYdGtUpcN4qXiUjl2XnHUUtYQipSerrvPEyFmIikF8LQh58Aolf7hXrckiIVsxxDT6G/M4VpNWKdkfDpISu4v2QpDqKGpfyCnOD/K8noFiYNX5XIHM6+1PDQ/2I6arTISw7eZkVvVtQyqZgI+zvzPfN9SEx9/Xhw9+/4dGxPIuJZ8i8DZTvP57y/cfz97kQTly9Rfn+4wmPiv3wfEvooCGREJOsers7LiUtz2hrbgfDHjP+wHnmtK5JDRfVOwCWBnq4mCp+X95wMzcmJiWNjNfTvj5IUiLy7GwwMlMplhiZIE9UszhQVw+payk0un2H1rKDaC07iLRlN6RO7mgtO4iktLdqvLYO0qp1kZ0+mLetYiT5SI8PsWjRIlxdXdHV1cXHx4fTp989j/evv/6iYsWKlChRAltbW/r06UNsbOHeo6KzKryXubk5jRo1YsGCBaSkpBS4nqWlYpVtZGTOraOQkBCVmAoVKnDsmPqFKB4eHmhra3PmTM5q+czMTIKDgylTpozKcXr37s2GDRuYO3cuy5YtA6By5crcvXsXKysrPDw8VB7GxnlXkAMEBATw8uVLlceYHu3eeZ7ampp4udgTdFN1Ll5Q6D0quavfWulDyVHMgfuSaGtqUNbJjqCwByrlQWEP8HYr2i3at8nlcm49fVGoRVbaWpp4ebgQFKK6sCco5CaVSnuoreNd2iNP/NkrN/DycEFLU/0onlwuJ+xBeJ5FVgA7j57G3NiIOlXybrNTILJseP4EibPqwiyJc2nkzx7kU0kNCSqrp/MNem/Mu2lralDWzpKge6rzlYPuPcXbKe8UiTf2X73L2B3HmdWxIXVKq/+9XHn6CktOXGJZr+aUc1C/TVPh89WkrLOd2uuDt4dTPrXezc3Wkr8nD2XnxO+Uj3oVS1O1lCs7J36HjZodMgqcr4YGZW3MCHqk+sEo6NFzvO0t8q23P/QRY/f/y6xWNajjkXcrqkoOFoTHJyN7a/DicVwilgZ6aGtofHC+ZGchf3wXqZfqln7SspWR3wvNG5+WSuaEb8maPEj5kJ3cjzzyCVmTByF/oDooI61SG7S0kJ1T/3fqS7NlyxaGDRvGuHHjuHLlCrVq1aJp06aEh6uff33mzBl69uxJ3759uXnzJtu2bePixYv069evUMcVnVWhQBYtWkRWVha+vr5s2bKFsLAwbt++zYYNG7h16xYaai42Hh4eODo6MmnSJO7cucP+/fuZPXu2SkxAQAAXL15k8ODBXLt2jVu3brF48WJiYmLQ19dn0KBBjBo1ikOHDhEaGkr//v1JTU2lb9++AEyYMIG///6be/fucfPmTfbt26fsyHbr1g0LCwtat27N6dOnefjwISdPnuSHH37g6VP1C3N0dHQwMjJSeRRkCkAv/5rsOHWRHacucj8iiumb9hIZm0CnetUAmLPtEKOXb1GpExYeQVh4BKnpGcQnpRAWHsG9Zy+Uzy/bd4KzN+/yJCqWB5FRrPnnNHuCLtPyq0rvzedj0dHXx6FieRwqKm7TWbi64FCxPKaOH6+TWBC9G1Zn+9nL7Dh7hfuR0czYeojI+Jd0qq2Yqzxn11HGrN6lUifsyXPCnjwnNT2DuKRUwp48515EzjY2C/cFcubmPZ5ExxP25Dk/r9/DrSfP6VTIxSq9Wzdh+5GT7DhyivtPIpi+4i8io2OV+6bOXruV0X8sVcZ3blKfiKgYpq/cyP0nEew4coodR0/xzdc5Uw8WbNrF6cvXefI8irAHjxk3byW3HobTuWk9lWPLZDJ2HTtNm/o10SzCH3x58DEkFWogKfcVmFkjqdcOjMyQX1V8UJTUaoWkWc7erZJKtcG9nGIPVRNLJOWqI6nSUGUPVUk1f3AuDcbmijZ96yPxqqbYOaCIevtVZPulMHYEh3E/Kp4Z+88S+TKJTlUV893n/PMvY7bldC72X71LwPbj/NS0BhUdrYlOSiU6KZWktJwpPytPXWHekQtMbVsXO1MjZUxKemae4xc6X38/tp++xI7TwdyPiGLG5v1Exr2kU52qinx3/MOYFdtU6iivD2npxL25PkREAaCjpYWng7XKw6iELvq6Ong6WKOdz4eeAudbtTTbr95nx9X73I95yYyjl4hMTKVTJcV8+TmBIYzZmzM/eX/oIwL2neOn+pWoaGdBdPIropNfkZSWs5C1cyVPEtLSmXbkEo/iEjl57xnLzoXSpXLR5+DLDu9AWqsJ0pqNwdYRjU4DwcyK7JP7ANBo+w0afUcpguVy5M8eqTxITECemaH4/1wLqKQ1myC7EqSYw/0JKa6R1Tlz5tC3b1/69etHmTJlmDt3Lo6OjixevFht/L///ouLiwtDhw7F1dWVmjVrMmDAAIKDgwt1XDFnVSgQd3d3rly5wrRp0wgICODp06fo6OhQtmxZRo4cyeDBg/PU0dLSYtOmTQwaNIiKFStSpUoVpk6dqjJHtWTJkhw+fJixY8dStWpV9PT0qFatGl26dAFgxowZyGQyevToQVJSEr6+vvzzzz+Ymirm5mlraxMQEMCjR4/Q09OjVq1abN68GYASJUpw6tQpRo8eTdu2bUlKSsLe3p4GDRpgZPTuhSOF1axaRRJSUlm05xjRL5PwtLdhyfDe2Fso8ox+mUhkbIJKnbYT5yn//+ajZ+z7NwQ7cxOO/T4GUKxU/2Xdbl7Ev0RXWwtXG0tm9u9Es2ofOIL2AZx9KzEi8IDy5w5/TAfg3Jq/WNtnUH7VPrqmvuVISH7F4v0niU5MxtPOiqXfdcP+9R6VMS+TiYxTvbXe7tecDuLN8Ej2X7yOnZkxR6cNAxSL1yb+tY+YxGQM9XQo42jLupG9qeBauA3Km9WqRkJSMgu3/E10XAKezvYsnTACeyvFKFR0/EsionOmFjjYWLJ04o/MWLGRjfuPYWVmwrj+3VX2WE1KSWXiwtVEx7/EUF+PMm7OrJ8+lgolVecqB129SUR0LG0b1i5UzrnJb18GPX0kNZoi0TdSfCnAjkWQ+DpvA2MkhqZvTQGUIK3VWtERlcsUG/6f+ht5yFt7BmtpI23UCQxMICtTsSXW/jWKYxVR0woeJKSmsfjEJaKTUvC0NmNpz+bYmyrmp8ckpRL51rSRrRdDyZLJmLL3NFP25tyybFOpFNPaKz5UbDp/k8xsGcM2HVY51uD6vnzXoPB716rkW7UCCcmpLN574vX1wZqlP/RUXh9iEpLyvn8nL1T+/83HEew/fxU7cxOOzhpVpFwKlG8ZZxJepbP47A2iU17haWHM0g51sX+9x2pM8isiE3OmYWy9co8smZwph4OZcjinE9KmnCvTWnwFgK2RPis61WPGscu0WXkAa8MSdPctRb/qZSgq2cWTYGCERstuaBgrvhQg68+fIVbRucfEDInZB4yUW9sjLVmezNljipzjxyYthimrGRkZXLp0iTFjVF8Pf39/goKC1NapUaMG48aN48CBAzRt2pSoqCi2b99O8+b5f8mFOhK5/D0z6AXhCycL2vX+oE/IYL9exZ1CoSw8vqS4UygUqV0Bt3P6RMgKuDXPJ8X1M9vxwua/vdNQZHfV70f7qco+8+4vRvjUaK88/P6gIjpgYfv+oAJo8OxRnkXFOjo66Ojk3bItIiICe3t7zp49q1zIDDBt2jTWrl3L7dvqF6Bt376dPn36kJaWRlZWFq1atWL79u1oaRX8CyHENABBEARBEITPiOQj/aduUfH06dPffex3LHrOLTQ0lKFDhzJhwgQuXbrEoUOHePjwIQMHDizU+YppAIIgCIIgCJ+RjzULICAggBEjRqiUqRtVBcXe6hoaGjx/rrr4LioqCmtra7V1pk+fjp+fH6NGKaavVKhQAX19fWrVqsXUqVOxtS3YCLEYWRUEQRAEQfgCqV1UnE9nVVtbGx8fH44cOaJSfuTIEZVpAW9LTU1VbmP5xpsF2YWZhSpGVgVBEARBED4jxfVVqSNGjKBHjx74+vry1VdfsWzZMsLDw5W39QMCAnj27Bnr1q0DoGXLlvTv35/FixfTuHFjIiMjGTZsGFWrVsXOzq7AxxWdVUEQBEEQhM9IcX1/VadOnYiNjeWXX34hMjKScuXKceDAAZydFXsXR0ZGquy52rt3b5KSkliwYAE//vgjJiYm1K9fv9Bfzy46q4IgCIIgCJ8RaTF+3ergwYPVblcJsGbNmjxl33//Pd9//32RjinmrAqCIAiCIAifLDGyKgiCIAiC8BkpvnHV4iE6q4IgCIIgCJ+R4lpgVVzENABBEARBEAThkyVGVgVBEARBED4jX9jAquisCoIgCIIgfE4kX1h3VUwDEARBEARBED5ZYmRVEARBEAThMyL9sgZWRWdVEARBEAThc/KF9VVFZ1UQ3keenVXcKRTKwuNLijuFQhlSf2Bxp1AoC3dNK+4UCkXi37a4Uyg0+fnjxZ1CoUgr1S7uFApFFn6/uFMoFM0fJxZ3CkIxE51VQRAEQRCEz4gYWRUEQRAEQRA+WV/abgCisyoIgiAIgvAZEd9gJQiCIAiCIAifCDGyKgiCIAiC8Bn50kYaRWdVEARBEAThM/KFzQL44jrngiAIgiAIwmdEjKwKgiAIgiB8RiRf2Aor0VkVBEEQBEH4jHxZXVUxDUAQBEEQBEH4hImRVUEQBEEQhM/IlzayKjqrgiAIgiAIn5Evbc6qmAYgCIIgCIIgfLJEZ/UT9ejRIyQSCSEhIf/T4wQGBiKRSEhISPifHkcQBEEQhI9DKvk4j8+FmAZQTHr37s3atWuVP5uZmVGlShVmzZpFhQoVii2vwMBA6tWrp/zZwsICX19fZsyYQcWKFYstr8/BphPnWfXPaaITkvGws2JM52b4lnRRGxudkMSsrQe5+TiCx1GxdG9QnYDOzfNt+8CFa4xctpX63mVY8F23j5Nv4EVWHQki+mWSIt8OjfH1dFaf78skZm0/zM3wSEW+9aoR0LGJSsyuoBDGrfs7T90r88eho/XfXGo8atXAf9QPOPl4Y2Jny+I2Xbj69/7/5Ni5bTp3jVUnrxCdlIKHtRljWtbC19VebeyRG/fYfO4GtyKjycjKxsPanCENq1KzVM6/x93nsSw4cp6bz6KIiE9iTIta9Kzl/UG5bfznJKv2HCU64SUeDrYE9O6AbxmPfOMvhN5h5tod3HsaiZWpMX1bNaKzf22VmLX7j7P58CkiY+IxNdLHv1plRnRtjY62FgApr9L4c8tejl64StzLJMq4OjC2dwfKe7h80DlsCrnPqou3iU5Jw8PciDH1KuLrYKk29sjdZ2wOuc+t6AQysmV4mBsxpEZZarrYqMStu3SXzVfvE5mUiqmuDv4l7Rleqzw6mhqFzm/jvsOs3LGP6LgEPJwdGPttT3zLlc43/sL1UGYs38C9x0+xMjelX7sWdG7eSG3s/pNB/DhzPg2q+7Jwwo/K8ovXw1i5Yx837z0gOi6BBT+PoGGNKoXOHWDTxTBWBV0nOukVHlYmjGlcDV9nG7WxR8IesTn4Freexynev1YmDKlTiZoeDmrjD9x4wMgdgdQv5cSCzg0/KL+NB4+zavchouMT8HC0J6BvF3zLlsw3/sKN28xcvZl7T55hZWZC3zZN6dyknkpMYkoqczfs4Mj5yyQmp+BgZclPfTpRx0fxN3nB5t0s3LJHpY6FiRGnV8/9oHMoCsnn1NP8CMTIajFq0qQJkZGRREZGcuzYMTQ1NWnRokVxpwXA7du3iYyMZP/+/cTHx9OkSRNevnypNjYzM/M/zu79/uucDl64zvTNBxjQrC47JgzGp6QzA/5cR0Rsgtr4jKwsTA31GdC8DqUc1P8BeONZbDy/bTuETz4dyQ/KN/gG07cdYkDTWuwYNwAfDycGLPiLiDj1/8YZmdmYGpRgQNNa78zXQFeHkzN/VHn8Vx1VAB19fZ5evcHm70b+Z8dU5+DVO0zfe5oB9X3ZMbQzPi52DFi1l4j4JLXxwQ8iqOHpyJI+rdg2tDNV3e0ZvHYfoc+ilTFpmVk4mBkxokkNLAxLfHBuB4KCmbFmOwPaNmHnzAB8yngwYNpCImLi1MY/jYph4PRF+JTxYOfMAL79ugnTVm/j8L9XlDF7T19gzsbdDOnQnP1/TGDqwO4cPHeJORtzPrz8vGQDQdduMfO7Xvw9exx+FcrwzZR5vIhLKPQ5HLz1hOknQhhQrQw7ejTEx8GCATvPEJGYqjY++Gk0NZytWdK2Jtu6N6CqoyWDd50l9EV8zjmEhTPn9HUGf1WWfb0bM6WxDwdvP+WP09cLnd+Bk+eYvmwdAzu1Ydf86fh6leLbCTOIiIpRG//0eRQDJszC16sUu+ZPZ0DH1vy6dC3/nDmfJ/bZi2hmrfgLX6+8Hd9XaemUdnVi/KA+hc75bQdvPGD6ofMMqFWRHQNa4+NkzYC/DhPxMlltfPDj59Rws2NJ10Zs+7YVVV1sGbzpKKGRsXnzT0jmt8MX8HGy/uD8Dpy5wIxVmxjQvgU7Z0/Cp6wnA6b8QUR03uMBPH0RzcCpf+BT1pOdsyfxbbsWTFu5kcPngpUxGZlZ9J30O8+iY/lz1GAOLJjGL4N7YW1motKWh6M9p1b9oXz8PfeXDz6PopBIPs7jcyE6q8VIR0cHGxsbbGxs8Pb2ZvTo0Tx58oTo6Gi18SdPnqRq1aro6Ohga2vLmDFjyMrKUj6fnp7O0KFDsbKyQldXl5o1a3Lx4kWVNg4cOEDJkiXR09OjXr16PHr0SO2xrKyssLGxoWrVqsyePZvnz5/z77//KqcnbN26lbp166Krq8uGDRsAWL16NWXKlEFXV5fSpUuzaNEiZXsZGRl899132Nraoquri4uLC9OnT1c+P2nSJJycnNDR0cHOzo6hQ4cqn5NIJOzevVslPxMTE9asWQPwwTl9TGuOnKVdTR/a1/bF3c6KgM7NsTU1ZnPgBbXx9hamjO3SnNY1KmGop5Nvu9kyGaOXb+O7VvVxtDT7ePke/Zd2fpVoX7My7raWBHRsosj35EW18fYWJozt1JTW1StiqJt/vhIJWBobqDz+SzcPHWHP+CmE7Nr7nx43tzWnQ2hXpSztq3rhbm1GQKva2BobsPlf9R2fgFa16VvXh/KO1rhYmDC8SQ2czU0IDHuojCnvaM2o5jVp5l0S7Q8Y6Xtj7b7jtK1fgw4N/HB3sGVs7w7YWJiw+fAptfGbD5/G1sKUsb074O5gS4cGfrSt9xWr9h5VxoTceUjlUu60qFkFeytz/CqWpbmfLzcfPAYgLSODI+dDGNm9DVXKeuJsY8V3HVvgYGXBpnyO+y5rLt2hXXlX2ldwxd3ciIB63tgalmDz1ftq4wPqedO3ainK25jhYmrI8FrlcTY1JPBBpDLmakQslezNaVHGCXtjffxcbGhW2pEbb3VoC5zfrv20869Hhyb1cXeyZ+yAXthYmrNp/xG18ZsPHMXWypyxA3rh7mRPhyb1aduoLqt2qt4VyM6WMeq3hXzfvT0OtlZ52qldxZthvTrh71e10Dmr5P/vDdpVKkn7yqVwtzQhoEl1bI312Xzxltr4gCbV6etXgfL2lriYGzO8gS/O5kYE3glXzV8mY/TOQL6rWxlHU8MPzm/tnn9o26AWHRrVxt3RjrF9u2JjbsbmQyfUxm/+JxBbC3PG9u2Ku6MdHRrVpm39Wqza/Y8yZuex07xMSmHBmO+oXMYTeysLfMqWpLSrk0pbmhpSLE2NlQ8zY6MPPg+h4ERn9RORnJzMX3/9hYeHB+bm5nmef/bsGc2aNaNKlSpcvXqVxYsXs3LlSqZOnaqM+emnn9ixYwdr167l8uXLeHh40LhxY+LiFCMmT548oW3btjRr1oyQkBD69evHmDFj3pubnp4eoDpaOXr0aIYOHUpYWBiNGzdm+fLljBs3jl9//ZWwsDCmTZvG+PHjlVMd5s2bx549e9i6dSu3b99mw4YNuLi4ALB9+3b++OMPli5dyt27d9m9ezfly5cv9GtY2Jw+loysLEIfR+DnpXobtYaXByH3w/OpVTCL9p7A1FCfdrV8i9TO2zKysgkNj8CvjLtKeY0yboQ8eFqktlPTM2gwdi71xsxh0MKNhIZHvr/S/zMZWdmEPovCz1P1j1yNkk6EPC7Y6yGTyUlJz8C4RP4fDD4styxuPgjHr2IZlXK/CmW4cvuB2johdx/iVyFXvHdZbj54TGZWNgCVS7tz80E41+49AuDJixhOXblBncrlAEUnK1smQ0dLS6UdHW0tLt9S38HM9xyyZYS+SMDPWXVkroazNSER6kfWcpPJ5aRkZGKsq60sq2xvQeiLBK5Fvr5eJiRz+uFz6rjaFi6/zCxu3nuIX2XV6Vx+lSpwJeyO2johYXfxq6QaX9OnIjfvPiDzrQGJhZt2YGZsSPvG9XI38dFkZGcTGhGLn7udSnkNN3tCnkYVqA2ZXE5KeibGuT6ILzoZgqm+Lu0q53+7/r35ZWZx8/5j/Ly9VMr9vL24cuue2joht+/nja/kxc37j5Sv7/GLIXiXcmfKsg3U7D2MlkPHs3T7PrKzZSr1Hke+oPY3w2k44CdGzF7Ck+cFe00+ti9tZFXMWS1G+/btw8BAMfKUkpKCra0t+/btQyrN+xli0aJFODo6smDBAiQSCaVLlyYiIoLRo0czYcIEXr16xeLFi1mzZg1NmzYFYPny5Rw5coSVK1cyatQoFi9ejJubG3/88QcSiYRSpUpx/fp1Zs6cmW+OsbGxTJ48GUNDQ6pWrUpqquI227Bhw2jbtq0ybsqUKcyePVtZ5urqSmhoKEuXLqVXr16Eh4fj6elJzZo1kUgkODvn3NIODw/HxsaGhg0boqWlhZOTE1WrFn5koLA5fSwJyalky2SYG6mOIpob6ROTz22zgrh89zE7z1xi54QhRU1RhSJfuZp8DYhJLFzH4W1uNhb82qsNJe2tSH6Vzobj5+n+2yp2/jwQF+u8H8D+v0pIfaV4fQ1Ub9WbG+gRk6T+NnVuq09f4VVmFk0qeH7c3BKTyZbJsDBWHdUyNzYiJiFRbZ2YhETMc40eWRgbkpUtIz4pGStTY5r7+RKfmET38bORIycrW0Zn/1r0b9MYAH09XbxLurJ4x0Hc7W0wNzFi/5mLXLv3CGcb9fNM8z2HV+lky+WY5+rIm+vrEPMorUBtrA6+w6vMbJqUyplT2ay0I3Gp6XTfrBidy5LJ6VzRjf7V8p9nqk58YqLiemBirJqfqTEx8eqn2UTHJ1DTNFe8iTFZ2dnEJyZhZWbK5Zu32fFPILsXTFfbxseSkPr69TXQU83HQI+Y+wV8/wbdULx/vVyVZZfDX7Dzyh12DmxTtPySkhTv4dyvr4kRMQnqX9+Y+JeYV8r1Hla+vslYmZnw9EU056+H0aJ2dZaOH8ajiBdMWbaBrGwZQzq1AqCCpxszfuiHi50NMQkvWbJtH10DprHnz6mYGv23d5G+tK2rRGe1GNWrV4/FixcDEBcXx6JFi2jatCkXLuS9dRwWFsZXX32l8gb18/MjOTmZp0+fkpCQQGZmJn5+fsrntbS0qFq1KmFhYco2qlevrtLGV199pTY3BwfFRTwlJQVPT0+2bduGlZWVctqAr2/OSF90dDRPnjyhb9++9O/fX1melZWFsbHigtK7d28aNWpEqVKlaNKkCS1atMDf3x+ADh06MHfuXNzc3GjSpAnNmjWjZcuWaGoW7u1Z2JzUSU9PJz09XaVMMyNTuUjkXXJfO+TyD//kmpKWzuiV25jcsw2mhvof1sh75M1XXqSNpiu6OVDRLeePf2V3J9pNW8pfgRcY16lpEVr+POV5fdWUqbM/5A6Ljpxnfq/meTq8H02uROTI3/nHT917++3yCzfvsHTnP4zv15mKni48fh7N9NXbWGRygMHtmwEw87vejFu8njoDx6IhlVLW1ZEWfr6EPnzygaeQ6xzkICnAO3h/WDiLgkKZ36YG5iV0leUXnkSx9HwYExpUpoKtGeEJyUw7EYLluVAGfVX2A/LLVSB/z2ucu+D1iyxBQnLqK0b9vpApQ/tj+h/dds79WiquDwV4fa/fZ9HJK8zv3ABzfUWHNyU9k9G7TjK5pR+mb73mH5P8fa9vnveLXKVcJpNjbmzEL4N6o6Ehxcvdhei4BFb+fUjZWa3tkzP6XdLZAe9SHjQeNJq/T5yld+vGH/uUhLeIzmox0tfXx8Mj59axj48PxsbGLF++nH79+qnEqvtFfPuXLfcvnrp6b2IK4vTp0xgZGWFpaYmRUd6Lo75+TgdKJlPcJlm+fDnVqlVTidPQUMytq1y5Mg8fPuTgwYMcPXqUjh070rBhQ7Zv346joyO3b9/myJEjHD16lMGDB/Pbb79x8uRJtLS0VM7vDXULqAqbkzrTp09n8uTJKmXje7dn4jcd861jYlACDak0zyhqXFJKntHLggqPiuNZTAJD5m9Qlslevwblv53A/qk/4GT1YaOVinwlHzVfdaRSCeWd7XgcpX7hzv9XJiX0FK9vrlHUuORX7+18Hrx6h/Hbj/FHtybUyDWN4KPkZmSgeK/mGkWNe5mEubH6OYQWJnlHXWMTk9DUkGLy+s7QvC17aVW7Kh0aKD4sl3Sy51VaOhOXbWRg2yZIpVKcbCxZP3kEqWnpJL9Kw8rUmOF/rMC+kO9jEz0dNCQSYlJUR1HjUtMx13/3tImDt54w/vAl/mhZnRq5phHMO3uTVmWdaV9BMRpY0tKY1MwsJh25zIDqZZAW8JOnqZGR4jXONYoam5CIuYn6jqalqUne+JeJaGpoYGJkwL3HT3n2IppBk39TPv/meuDVohsHl8/ByfbDFyy9zaTE69c3Odf7NyUtz2hrbgdvPGD8njP80aE+Ndxydr4Ij0/kWUIyQzblzHNWXs9+Wc3+79rhZFawTriJoeHr97Dq66V4D6tvw0LNqLby9X09GGBpaoympgYaGjl3Nt0cbImJf0lGZhbaahaKltDVwdPZgUeRLwqU+8f0hQ2sis7qp0QikSCVSnn16lWe58qWLcuOHTtUOp9BQUEYGhpib2+PmZkZ2tranDlzhq5duwKKDl1wcDDDhg1TtpF7odK///6rNhdXV1dMTEwKlLe1tTX29vY8ePCAbt3y31bJyMiITp060alTJ9q3b0+TJk2Ii4vDzMwMPT09WrVqRatWrRgyZAilS5fm+vXrVK5cGUtLSyIjc+b63b17Vzkdoag55RYQEMCIESNUyjQv7ntnHW1NTco62xEUeo+GlXNGYIJC71Hfu8w7aubPzdaCvyd/r1L2566jpKSlM7ZLc2zM8h8dfh9tTQ3KOtkRFPaAhpVy8gsKe0D9iqU+uN3c5HI5t56+wNM+70KQ/8+0NTUoa29F0N0nNCyXMy846G449cu65Vtvf8gdft52lN+6NqZOGdd844qWmyZebk4EXQujUVXvnNyu3aJ+FfVb5nl7uhJ4SXVh2NmrYXi5OaP1eqHXq/SMPB+UNaRS5HLFiPLbSujqUEJXh5fJqZy9GsbI7l8X7hw0pJS1NiHo8QsaeuZ0iIIev6C+h12+9faHhfPz4WB+a1aNOm5556GmZWbn2XdSQyJBjlwxyFnAzoG2liZeHq4EXblGo7e2jQq6cp361X3U1vEu48mJ85dVys5evoaXpxtampq4OdqxZ9Eslef/XLeVlFevFIu3LD7eNBttDQ3K2pkT9CCChmVccvJ/EEH9Uvl/gNp//T4/7znDb+3qUqeko8pzbhbG/D1I9d/5z+OXSMnIZGyT6tgYF/zukbaWJl7uzgRdDaXRW69n0NWb1K9aSW0d71LuBF4MUSk7G3ITL3cXtF7fwatcxpN9p/5FJpMpp+I9iniBpamx2o4qQEZmJg+eRuJT5sPn4H4oMQ1A+M+kp6fz/PlzAOLj41mwYAHJycm0bNkyT+zgwYOZO3cu33//Pd999x23b99m4sSJjBgxAqlUir6+PoMGDWLUqFGYmZnh5OTErFmzSE1NpW/fvgAMHDiQ2bNnM2LECAYMGMClS5eUK+qLatKkSQwdOhQjIyOaNm1Keno6wcHBxMfHM2LECP744w9sbW3x9vZGKpWybds2bGxslKv6s7OzqVatGiVKlGD9+vXo6ekp57XWr1+fBQsWUL16dWQyGaNHj0ZL6/235d+Xkzo6Ojro6KiOzmQXYApA70Z+jF65HS8Xe7zdHNl2KpjIuJd0qqv4YzVnx2GiEhKZ0be9sk7Y68VHqekZxCWlEBYeiZamBh52VuhoaeFprzpSYvT69lnu8g/Ru2F1Rq/ehZezHd5uDmw7fYnI+Jd0qq2YSjFn11GiEpKY0SfnD0zYk+dv5ZtK2JPnaGlo4GGnmHO4cF8gFV0dcLYyJzktnQ0nznPryXN+7tysyPkWlI6+PpYeOR1CC1cXHCqWJyUunvgnRVs8Vhi9a3kzessRvBys8HayYduFm0QmJNOpumLB0ZyDQUQlJjOjk2IqzP6QOwRsOUJAq1pUdLIhOikFAF1NTeVuERlZ2dx/PUqdmSXjRWIyYRHRlNDWwtnCpMC59WpRnzHz11LOzRnvkq5sPXqWyJh4OjWqpcht425exCUw87veAHT2r8XGf04yY+12OjTwI+TOQ3YeD+L3H75RtlnPpzxr9h+njKujchrAvC37qOdbHo3Xf/jPhIQiR46rnTWPn0fz+/pduNpZ83Vd9VOR3vn6+pRk9MELeFmb4m1nzrZrD4hMSqVTRcW//ZzT14lKfsWMpoq57/vDwgk4dJGAet5UtDMn+vWorK6mBoY6it/vuu62rL10lzJWpoppAPHJzAu6ST03OzQKuadl76+bM3r2Qsp5uuFduiRbDx0jMjqGzs0Ue4rOXr2JqNh4Zo4crHiNmzXkr72Hmb5sPR2b1Cfk1h12HD7B7z8pPrDqaGtT0kW1A2j4epT+7fKUV2mERzxX/vz0RTRh9x9hbGiAnZVFwfOvXo7Ru07hZWeBt4MV2y7dJvJlMp18FfN35xwNJiophRlf1wEUHdWA3acIaFKdig6WRL8eldXV1MRQVxsdTU08rUxVjmH0enFb7vKC6NWqMWP+XE45dxe8S7mz9chJImPi6NS4riK/9dt5ERfPzB8UU8A6N67LxgPHmLFqMx0a1Sbk9n12HjvN7yMGKNvs3KQeG/YfZdrKTXRr1oDHkS9YtmM/3Zs3UMbMWrOFur7e2FmaEfsykSXb9pGc+oo29WoU+hyEwhGd1WJ06NAhbG0Vn/ANDQ0pXbo027Zto27dunm2lLK3t+fAgQOMGjWKihUrYmZmRt++ffn555+VMTNmzEAmk9GjRw+SkpLw9fXln3/+wdRUcTFwcnJix44dDB8+nEWLFlG1alWmTZvGN998Q1H169ePEiVK8Ntvv/HTTz+hr69P+fLllaO6BgYGzJw5k7t376KhoUGVKlU4cOAAUqkUExMTZsyYwYgRI8jOzqZ8+fLs3btXuSvC7Nmz6dOnD7Vr18bOzo4///yTS5cuFTmnj6lp1fIkpKSyeO8Jol8m4WlnzdIfemBvrnjtY14mEZlrz9V2vyxU/v/NxxHsP38NO3MTjs783+8R2tS3HAnJr1i8/yTRicl42lmx9Ltu2JubvM43mchce662+3VpTr7hkey/eB07M2OOThsGQFJqGhP/2kdMYjKGejqUcbRl3cjeVMhnI/z/BWffSowIPKD8ucMfisUo59b8xdo+g/6zPJpWLElCahqLj10gOjEFTxtzlvZpib2p4jZlTFIKkQk50zC2nr9BlkzGlN0nmbL7pLK8jU9ppnVUbAwfnZhCuz83K59bfeoKq09doYqbPWsH5CwsfJ9mNXxJSEph0Y4DRMcn4uloy5KAwdhbKn7fouMTiYzJ2a7JwcqCJQGDmbF2Bxv/OYWVqTFj+3TAv3rOKNbAdk2RSCTM27yXF3EJmBkZUNenPMO6tFLGJKW+4o9Nf/M8NgFjgxL4V6vEsC6tlKOzhdG0tCMJaRks/jeM6JQ0PM2NWNq2JvZGihG6mJQ0It/ac3XrtQdkyeRMOXaFKcdy9odt4+XMtCaKD5QDq5dBgoQ/z94gKvkVpno61HOz44eaqqvIC6JZna9ISEpi4cadRMcl4OniyNLJo7G3Vnywi45PICI6Z89VBxsrlv7yEzOWrWfjvsNYmZsybkAvGteslt8h1Lpx9wG9xkxR/jxj+XrFeTaszYwRBX//Ny3nRsKrdBafDCE6ORVPK1OWdvPH3kQx7SMmOZXIlynK+K2Xbite3wPnmHLgnLK8TUUPprWpnaf9ompWsyoJScks2rqH6PiXeDrZs+TnYdi/7pBHx78kMjpn+pGDtSVLfh7OjNWb2HjwOFZmJozt2xX/r3LWOdhamLFi4o/MWL2ZNsMnYG1mSo8WDen3dc6H7eex8Yycs4SEpGRMjQypWNKdzTPHKY/7X/rCBlaRyAszkVEQvkDZp7cVdwqFk/XpfUnDuwypP7C4UyiUhbumFXcKhSJx/bCpKMVJfv54cadQKNIG7Yo7hUKRnVe/3+unSuJds7hTKBRpWb/3BxXRLQ/39wcVQOl7H74DzH9J7LMqCIIgCIIgfLLENABBEARBEITPyJc2DUB0VgVBEARBED4jYjcAQRAEQRAE4ZMl+cImcX5hpysIgiAIgiB8TsTIqiAIgiAIwmdETAMQBEEQBEEQPllfWF9VTAMQBEEQBEEQPl1iZFUQBEEQBOEzIqYBCIIgCIIgCJ+sL6yvKqYBCIIgCIIgCJ8uMbIqCIIgCILwGZF+YUOrorMqCIIgCILwGfnC+qpiGoAgCIIgCILw6RIjq4IgCIIgCJ8RsRuAIAiCIAiC8Mn6wvqqorMqCO+jUaFOcadQKPLnD4o7hUJZuGtacadQKEO+HlvcKRTKgu8+r/cvAAYGxZ1BocjuXC7uFApFo83A4k6hUGQPrhZ3Cp+cL62zKuasCoIgCIIgCJ8sMbIqCIIgCILwGZFIv6yhVdFZFQRBEARB+IyIaQCCIAiCIAiC8IkQnVVBEARBEITPiFQi+SiPD7Fo0SJcXV3R1dXFx8eH06dPvzM+PT2dcePG4ezsjI6ODu7u7qxatapQxxTTAARBEARBED4jxTUNYMuWLQwbNoxFixbh5+fH0qVLadq0KaGhoTg5Oamt07FjR168eMHKlSvx8PAgKiqKrKysQh1XdFYFQRAEQRCE95ozZw59+/alX79+AMydO5d//vmHxYsXM3369Dzxhw4d4uTJkzx48AAzMzMAXFxcCn1cMQ1AEARBEAThMyKRSD7KIz09ncTERJVHenq62mNmZGRw6dIl/P39Vcr9/f0JCgpSW2fPnj34+voya9Ys7O3tKVmyJCNHjuTVq1eFOl/RWRUEQRAEQfiMSCQf5zF9+nSMjY1VHupGSAFiYmLIzs7G2tpapdza2prnz5+rrfPgwQPOnDnDjRs32LVrF3PnzmX79u0MGTKkUOcrpgEIgiAIgiB8gQICAhgxYoRKmY6OzjvrSHJNmJXL5XnK3pDJZEgkEv766y+MjY0BxVSC9u3bs3DhQvT09AqUp+isCoIgCIIgfEby6xwWlo6Ozns7p29YWFigoaGRZxQ1Kioqz2jrG7a2ttjb2ys7qgBlypRBLpfz9OlTPD09C3RsMQ1AEARBEAThM/KxpgEUhra2Nj4+Phw5ckSl/MiRI9SoUUNtHT8/PyIiIkhOTlaW3blzB6lUioODQ4GPLTqrnzCJRMLu3bvzfd7FxYW5c+d+1GP27t2bNm3avDOmMMdds2YNJiYmRc5LEARBEASFj7XAqrBGjBjBihUrWLVqFWFhYQwfPpzw8HAGDhwIKKYV9OzZUxnftWtXzM3N6dOnD6GhoZw6dYpRo0bxzTffFHgKAIhpAMUqKiqK8ePHc/DgQV68eIGpqSkVK1Zk0qRJfPXVV++tf/HiRfT19Qt0rEmTJjF58uR3xjx8+LBAbRXmuP9fyeVyFixfzZbde0hMSqKiV1kmjBqBp7vrO+v9czyQP5euIPxpBE4Odgwf+C2N6tVWPp+VlcX85avZe+gIMXGxWJqb83WLpgz+phdSqZTMrCzmLl7OqaB/efIsAgMDfWpU8eXH7wZibWmR73E3HjjGyp0HiI5/iYeTHWP7dcPXq1S+8Rdu3GLGyo3cC4/AysyEfm2b0blpfeXzO4+dZuyfK/LUu7p9OTra2gDU7/cjEVExeWK6NmvAhIE985S/z6Zz11h18grRSSl4WJsxpmUtfF3t1cYeuXGPzeducCsymoysbDyszRnSsCo1SzkrY+4+j2XBkfPcfBZFRHwSY1rUomct70LnVVQetWrgP+oHnHy8MbGzZXGbLlz9e/9/noekVjOkDdqCkSlEhpO9czncD31/RdcyaPwwHSIfkz3zB/VtV66FRp+fkF37F9nyXz9OvtUbIa3VAgxNIOop2fvWwaPb6oOdS6HRpAtY2YGWDsRHI7twDPnZgzkxUg0kdVsjrVxb8RrERCI7tAn5nasfJd9NZ66w6vhFohOT8bCxYMzX9fF1Vz+yFP0ymVl/B3LzyXMex8TTvZYPAW3r54lbFxjM5rMhRCYkYaqvh3/FkgxvURsdraL/aZfL5SxYupwtO3YrrnHlvJgQMApPd/d869y9f595i5ZxM+wWzyIjCRg5nN7duqjEXLx0mZXrNnAj9BbRMTEsnDOLhvXqFjq/jYdOsOrvfxTXNEc7Avp0wrdsyXzjL9y8zcw1W7n3JAIrUxP6tmlM58Y5x+054Tcu3ryTp17tyuVZOm4oAAu27GHh1r0qz1uYGHF65exC5/+56tSpE7Gxsfzyyy9ERkZSrlw5Dhw4gLOz4toaGRlJeHi4Mt7AwIAjR47w/fff4+vri7m5OR07dmTq1KmFOq7orBajdu3akZmZydq1a3Fzc+PFixccO3aMuLi4AtW3tLQs8LFGjhyp/OQDUKVKFb799lv69+9f6PYKc9z/r5av28jqTVuYMWEsLk6OLF61lj7fD+fQto0Y6JdQW+fKtRsMHzeJHwb0pWHd2hwNPMWwsRPYuHwhFct5KdvdvPNvZk4ci4ebKzfCbhEwZTqGBgb06tyBtLQ0Qm/fYdA3vShd0oPExCSm/TGPQT+OYee6vJ1HgAOnzzN9xV9MGNiTymVKsuXQCb6dPJt9C6djZ2meJ/7p82gGTJ5NB/+6/DZiIJfD7vDLknWYGhvSuEYVZZxBCT0OLp6hUvdNRxVg++yJZMtkyp/vPn7GNxNm0divCoV18Oodpu89zYQ2dankbMvW8zcYsGove0d0w87UME988IMIang6MqzJVxjq6bArOJTBa/exeUhHytor3r9pmVk4mBnRuLwHM/a9+xtY/pd09PV5evUGQas3MHDnX8WSg6RyTaRt+yHbugT5g1Ckfk3QGDSJ7F+HQHx0/hV1S6DRYzjyO1eRGJqojzG1RNrmG+T3bny8fMtXR9q8J7K/VyF/fBtptYZo9B5D9h8j4WVs3goZ6cj+PYw8Mhwy0pC4lEb6dV9kGenILx4HQOrfEYl3TWS7liOPikBSsgLS7iPIXjwRIh8VKd+Dl28xfddxJrRvRCVXe7YGXWXA0u3sDfgGO1OjvOlmZWNqoMeARtVZe/KS2jb3BocyZ98ppnZpQiUXex5FxzF2o6LzPebrvB3bwlq+Zh2rN2xixuQJuDg7sXj5KvoM/J5Du7dhkM9gxau0dBwc7GnSqAHTZ/+hNib1VRqlSnrStlVLvh85+oNyO3D2IjNWb2F8/25ULu3BlsMnGfDrPPbOnaz+mvYimoG/zqN9w1rM+qEfl2/dY8ryvzAzMsT/Kx8A5o0aTOZbG9UnJCXz9Y+/0OT18294ONqxamLOgiQNafHcoJYU433xwYMHM3jwYLXPrVmzJk9Z6dKl80wdKCwxDaCYJCQkcObMGWbOnEm9evVwdnamatWqBAQE0Lx5c7V1fvnlF6ytrQkJCQHy3o6XSCSsWLGCr7/+mhIlSuDp6cmePXsAxacbGxsb5UNDQwNDQ8M8ZW/8/vvv2NraYm5uzpAhQ8jMzFQ+l/u4CQkJfPvtt1hbW6Orq0u5cuXYt2+f2nOIjY2latWqtGrVirS0NAIDA5FIJBw7dgxfX19KlChBjRo1uH1bdYRk7969+Pj4oKuri5ubG5MnT1b5BoxJkybh5OSEjo4OdnZ2DB06VPncokWL8PT0RFdXF2tra9q3b//uf5z3kMvlrNu8lYG9e+Jfrw4l3d2YOXEcaWnp7Psn/1/ItZu3UaOqLwN698DdxZkBvXtQvYoPazdvU8aEXL9Bg9o1qVuzBg52tjRpUI+a1apyI+wWAIYGBqxe8AfNGtXHzdkJ7/Je/DxyGDdv3Sbi+Qu1x13z9yHaNaxNB/+6uDvaMbZ/N2wszNh04Jja+M2HjmNrac7Y/t1wd7Sjg39d2jaszapdB1XiJBIJlqYmKo+3mRkbqTwXeDEEJxsrqpYrXZCXWfUcTofQrkpZ2lf1wt3ajIBWtbE1NmDzv9fVxge0qk3fuj6Ud7TGxcKE4U1q4GxuQmBYzt2D8o7WjGpek2beJdHW1FDbzn/h5qEj7Bk/hZBde98f/D8irdcG+bkjyM8dhhdPke1cAfExSGs2fXe9zkOQXzoJD2+pD5BI0eg1EtmBjchj1b8/PyjfWs2RB59AHnwCoiOQ7VsHL2ORVm+kvkLkI+RXgyDqKSTEIA85g/zONSSuOe9FSaVayAJ3I78dAvFRyM8fRX7nKtJa6q/HhbEmMJh21crT/qsKuNuYE9C2PrYmhmw+E6I23t7cmLFtG9C6ajkMddUvfrn6KIJKrva08CmLvbkxfqVdaVa5DDeeqN9CqDDkcjnrNm5mYN/e+DeoR0kPd2ZOmUhaWhr7Dv6Tb70KXmUZPXwozZv4o62lrTamTs0aDB8yCP8G9T44v7V7j9C2fk06NKyFu4MtY7/pjI25KZv/Oak2fvPhk9hamDH2m864O9jSoWEt2tb3Y9Wew8oYE0N9LE2NlY+ga2Ho6mjTuIavSluaGlKVODPjvB+W/wvFNQ2guIjOajExMDDAwMCA3bt357sB7xtyuZwffviBlStXcubMGby9vfONnTx5Mh07duTatWs0a9aMbt26FXik9o0TJ05w//59Tpw4wdq1a1mzZo3aT0ug2JaiadOmBAUFsWHDBkJDQ5kxY4ZKx/eNp0+fUqtWLUqXLs3OnTvR1dVVPjdu3Dhmz55NcHAwmpqafPPNN8rn/vnnH7p3787QoUMJDQ1l6dKlrFmzhl9/VdxO3L59O3/88QdLly7l7t277N69m/LlywMQHBzM0KFD+eWXX7h9+zaHDh2idu3aFMXTiEiiY+OoWT1nhFBbW5sqlb25ci3/0aOQ6zeoWU11VLFW9aoqdXy8K/Bv8CUePlbcRrl15x6Xrl6jTo38p4UkJ6cgkUgwMjDI81xGZhY37z3Cr1I5lXK/SuW4cuue+jxv3csTX7NSOW7ee6Qy8pD6Ko36fUdQp88wBvwyh9D7j/PNMSMziz2BQbRtWLvQF8iMrGxCn0Xh56n6VX41SjoR8jiyQG3IZHJS0jMwLlGwVa9fFA1NcPRAfuuKSrH81hUkrmXyrSap1gCJhS2yg5vyjZE27Yw8+SXyf4s2qqJCQwPsXJHfvaZSLL97DYlT/reBVdi6IHEuifxBWE6ZpiZkZarGZWUiccl/ukxBZGRlE/r0OX6lXVTKa5R2IeTRsw9ut7KbPaFPXnDt9e/Ak5gEToc+oE7Z/G/TF9TTZxFEx8RS86vqyjJtbW2q+FTmytVr76j5v5eRmcXN+4/x8y6rUu5X0Ysrt++rrRNy+wF+Fb1U4729uHn/sco17W07jp2hmV8VSuT6sPA4Mora/UbScNAYRsxZxpPn77jzIHw0YhpAMdHU1GTNmjX079+fJUuWULlyZerUqUPnzp2pUKGCMi4rK4uePXsSHBzM2bNn37t6rnfv3nTpopgjNG3aNObPn8+FCxdo0qRJgXMzNTVlwYIFaGhoULp0aZo3b86xY8dUpgy8cfToUS5cuEBYWBglSyr+ULi5ueWJu3PnDo0aNaJ169b8+eefeTosv/76K3Xq1AFgzJgxNG/enLS0NHR1dfn1118ZM2YMvXr1UrY/ZcoUfvrpJyZOnEh4eDg2NjY0bNgQLS0tnJycqFq1KgDh4eHo6+vTokULDA0NcXZ2plKlSgV+LdSJjlXcZjR//dVxb1iYmRIRmf+oRkxsXJ465mZmRMfmfJjo37MbScnJNO3YHQ2plGyZjOGD+tOicUO1baanp/P7giW0aNwQA4O8t+biE5PIlskwNzFWKTc3NiYm4aX680t4SU3jXPEmxmRlZxOfmIyVmQlu9rZM/6EfJV0cSU59xbq9h+k6eiq7503Bxc4mT5vHzl8iKSWVrxvUVP/ivENC6iuyZXLMDVSnV5gb6BGTlFqgNlafvsKrzCyaVCjYNilfFH0jJBoayJMSVIrlSQlIjEzU17G0RdqqF9lzx8BbUz1UuJZBUr1RvvNYP1iJ1/kmq75/5ckvkRga51NJQWPMAtA3AqkGsmPbFSOzb+rfuYa0ZnOyH96CuBdI3MshKeMDRbzNm5Dy+v1rqPr7aW6oT0xiyge326xyGeKSX9F93kaQQ5ZMRmc/b/o3rFakfAGiY/K5xpmbERFZsA+I/ysJSclky2RYGKtOnzA3Mcz3mhaT8BJzE9URUAtjI8U1LSkZq1x3ha7dfcjd8GdMHdxLpbyCpyszvv8GFztrYhISWbJjP13HzWDP3MmYGuYdLPifkn4+o6IfgxhZLUbt2rUjIiKCPXv20LhxYwIDA6lcubLKKObw4cM5d+4cp0+fLtA2D293dPX19TE0NCQqKqpQeXl5eamMjNra2ubbRkhICA4ODsqOqjqvXr2iZs2atGnThnnz5qkdWXs7b1tbWwDlMS9dusQvv/yiHI02MDCgf//+REZGkpqaSocOHXj16hVubm7079+fXbt2KacINGrUCGdnZ9zc3OjRowd//fUXqan5d3DUffXczr0HqFTHX/l403bu05DL5e/dCyTPZsqobqZ84Mgx9hw8wuwpE9i5fiUzJo5l1YbN7Np3MHdTZGZlMXzcJORyGZN++rFQxwU5EvLPNW+4XKXcu7QHrer5UdrVCV+vUsz9aQgu9jZs2HdUbXvbj5yilk8FrM1N35nnu+R5vdXlqcb+kDssOnKe2V0b5+nwCm95/W+cI58XVyJFo9coZAc2QnSE+hgdPTR6/Yhs8wJISfyoaeZPouYcVGUvnUz2gnHIdq9E6tcUScWc7XZk+9Yij4lEY8RsNKasR9qqt2KKQ36d8cJnp+JdG6kXxIW74Sw9co4J7RuxfWRP5n3TmsCb91n8j/qvvXyXPQcOUalGHeUj5xqXd/P3Qu939L+SJzfec03Lfe19Xa6mzo5jZ/B0sqeCp+qC2dqVy+P/lQ8lnR2oUbEsS8Yqppv9faLwr3mRFcfeVcVIjKwWM11dXRo1akSjRo2YMGEC/fr1Y+LEifTu3RtQdLY2bdrEP//8Q7du3d7bnpaWlsrPEokEWSEvtoVpoyBbT+jo6NCwYUP279/PqFGj1Ha63z7mm4vKm2PKZDImT55M27Zt89TT1dXF0dGR27dvc+TIEY4ePcrgwYP57bffOHnyJIaGhly+fJnAwEAOHz7MhAkTmDRpEhcvXlS7pdb06dPz7JowdsQwdm9Ypfw5I0NxqzAmNg4ri5wV+LHxCVjkGol4m4W5GTGxqos/4uLisTDL6cDNmreYb3t1o7m/YiS1lIc7EZEvWLp2A1+3yJk/mJmVxbCACTyNiGTtoj/VjqoCmBoZoiGVEhOfoFIe+zIRc5O8CzsALE3yjrrGvkxEU0MDk3xGD6RSKeU9XXkckXdk+VlUDOeu3mT+mKFqar6fSQk9NKSSPKOoccmv3tv5PHj1DuO3H+OPbk2okWsagfBaSiLy7GwkRqa83dWTGBpDYkLeeF09JM6eSB3coMPrRZsSCRKpFI25u5EtmoA8JQmJuTXSb8e/1aDi91pj7m6ypw6EmA+cW5n6Ol8DY9V8DYwg+T0d49eLxeQvniAzMEbaoB3ZV193NFKSkG2YA5paUMIAEuORNuny7gVmBWCi/+b9qzqKGpecirnhh394mnfwDK18vWj/leKDfkk7S1IzMpm05TADGn2FtBAjb/Xr1FIu8gTIyMwAICY2Fqu3dhmJjYt/5zXuv2BiaKC4puW6RsW9TMr3mmZhYkxMvOp7I+eapnrtfJWezoGzF/m+U6v35lJCVwdPJ3seRRZuQEgoPDGy+okpW7YsKSk5F7VWrVqxceNG+vXrx+bNm4sxM/UqVKjA06dPuXMn75Yfb0ilUtavX4+Pjw/169cnIiKf0Zh8VK5cmdu3b+Ph4ZHnIX19i05PT49WrVoxb948AgMDOXfuHNevKxbfaGpq0rBhQ2bNmsW1a9d49OgRx48fV3usgIAAXr58qfKYMHoEzo4OyoeHmwuW5macPX9RWS8jM5OLl0OoVKGc2nYBvMuX4+yFYJWyM+cvqtRJS0vLMwKgoSFF/taHhTcd1cdPnrJm4R+YmuR/61NbSxMvDxeCQm6qlAeF3KRSaQ/1eZb2yBN/9soNvDxc0NJU//lWLpcT9iA8zyIrgJ1HT2NubESdKhXzzfNdtDU1KGtvRdDdJ6rncDccb2fbfOvtD7nD2K1HmdXFnzpl3r2l2BctOwue3ENSWnV6jKSUN/KHYXnj01LJmjaE7JlDlQ/52UPIXzxV/P+j2/Diad6YGxeQ371O9syhEJ93S7OC55sNEQ+ReFZQKZZ4lEcenv91KA8Jio5pblmZkBiv2MqqXFXkocF5YwpBW1ODsg42BN1WndMddPsx3i7qt14riLSMLKS5rxUSKXIUd2wKw0BfH2cnR+XDw80NSwtzzv57XhmTkZnJxUuXqVSxwjta+t/T1tLEy92ZoKuq782ga6FUKqV+vq53KTeCrqluw3Y2JBQvd+c817RDZ4PJyMykZZ3qvE9GZiYPnkZiafru6Sf/C1/aAisxslpMYmNj6dChA9988w0VKlTA0NCQ4OBgZs2aRevWrVViv/76a9avX0+PHj3Q1NQs8mr2j6lOnTrUrl2bdu3aMWfOHDw8PLh16xYSiURlnqyGhgZ//fUXXbp0oX79+gQGBmJjk3duozoTJkygRYsWODo60qFDB6RSKdeuXeP69etMnTqVNWvWkJ2dTbVq1ShRogTr169HT08PZ2dn9u3bx4MHD6hduzampqYcOHAAmUxGqVLqF02o/eo5eZrKjxKJhJ6dO7J0zQZcHB1xdnJg6er16Orq0KJxzmrknyZOxdrKgh+HKEafenZuT/cB37Ns7V80qFOTYyfPcO5CMBuXL1TWqVerBkvWrMfOxhoPN1fCbt9l9cYttGupWJGclZXF0DHjCb11h6VzZpKdLVPOLzM2NkJbK+8f396tmzD6j6WU83DFu7QHW/85QWR0rHLf1NlrtxIVF8/M4QMA6NykPn/tP8r0lRvp6F+XkFv32HH0FL+PHKRsc8GmXVQs5YGLnTXJqa9Yv/cItx6GM2FgD5Vjy2Qydh07TZv6NdFUs+iuoHrX8mb0liN4OVjh7WTDtgs3iUxIplN1RUd/zsEgohKTmdHJH1B0VAO2HCGgVS0qOtkQ/XpUS1dTE0M9xb9vRlY296MU84Uzs2S8SEwmLCKaEtpaOFuYfHCuhaWjr4+lR848bwtXFxwqliclLp74J0//kxxkJ3Yj7TECSfhd5A9vIfVrAmaWyM4opp9IW/YEE3Nk6/9Q3G+NDFdtICkBMjNUy3PHvEpRX/4h+Z7ej7TjECRPHyAPv4O0agMwsUB2XjENRdq4MxiZItu2GFDsyUpCLPLX0xYkLqWQ1mqBPOitle2O7kiMzJBHPAZjU6QN2oNEguxU0Xdp6F3Xl9F/7cfL0QZvFzu2nbtKZHwinfwUH+Dm7D1F1MskZnTP2Xkg7Kli94TUjAziUlIJe/oCLU0NPGwUI511vdxZGxhMGQcrKjjbEh6TwLyDZ6jn5V7k7ZQkEgk9u3Zm6co1uDg54uzkxNKVq9HV1aVF08bKuJ9+noi1lRU/Dh0CKDpv9x88VP7/i6howm7foYSeHs5OjgCkpKYS/tb7+umzCMJu38HYyAg724L9TejVshFj5q2knLsz3qXc2XrkFJExcXTyV6x7mLNhJy/i4pk5tC8Anf3rsPHgCWas3kKHRrUJuX2fncfP8PuwvOswdhw/Q4OqldTOQZ21dht1fStgZ2FG7MsklmzfT/KrNNrUVf/tTf9TX9icVdFZLSYGBgZUq1aNP/74g/v375OZmYmjoyP9+/dn7NixeeLbt2+PTCajR48eSKVStbfEi8uOHTsYOXIkXbp0ISUlBQ8PD2bMmJEnTlNTk02bNtGpUydlh7UgGjduzL59+/jll1+YNWsWWlpalC5dmn79+gFgYmLCjBkzGDFiBNnZ2ZQvX569e/dibm6OiYkJO3fuZNKkSaSlpeHp6cmmTZvw8vJ6z1HfrX/PrqSnpzN51mxeJiVT0asMq+bPUdljNfLFC5VbcZUrlGfO1InMXbKCeUtX4Ohgzx/TJqvcfvt55HD+XLqCybPmEBsfj5WFBZ2+bs2Qfr0BeB4VzfFTZwBo3b2PSk7rFs+jmk/exWPNalUjISmZhVv+JjouAU9ne5ZOGIG9leKPXnT8SyKicxZ5OdhYsnTij8xYsZGN+49hZWbCuP7dVfZYTUpJZeLC1UTHv8RQX48ybs6snz6WCiVVRzaCrt4kIjqWtg2LtgND04olSUhNY/GxC0QnpuBpY87SPi2xf71HZUxSCpEJOV/nt/X8DbJkMqbsPsmU3Tnb2bTxKc20jooPFNGJKbT7M+duxepTV1h96gpV3OxZO+C/+/1y9q3EiMADyp87/DEdgHNr/mJtn0H5Vfuo5JfPINM3QtqkMxiZKTb4Xzw55xa4sRkS009nf2X59X+R6RsqvsTA0ARePCF7zUxIeD1ia2iCxOStL8mQSBUdWDNLxRzU2BeKDf8vvLV9m6Y20kYdwcwKMtKR375C9tZFkFawRXzv0rRyaRJSX7H4nyDF+9fWgqUD2mFvphiRi0lMJjI+SaVOu9/XKf//5pMX7L8Uhp2pEUcnKj5UDvT/CokE/jxwhqiXyZjq61GvnDs/NKtV5HwB+vfuqbjGTZ/Fy0TFlwKsWjxfZY/VyOcvlHe3AKKio2nTubvy51XrNrBq3Qaq+lRm/YolANwIDaNn/5z39fTZcwH4umVzZvwysUC5NfOrQkJSMou27SM6/iWeTnYsGTsUeyvFHqvR8QlExrx1TbO2ZMm4ocxYvZWNhwKxMjNm7DedlXusvvEw4jmXwu6xYsJwtcd9HhvPyD+Wk5CUjKmRIRU93dg8PUB5XOF/RyKXv2dGuiB86V5+XvOR5M8fFHcKhSL7P/buOyqK623g+HcXBJRepRcBFbGgYAN7b4k9amKiiSbYEqMxUfRnN1FjjSaWGLEkRuy994ZdEBUs2FBBAekobXffP1YXFxYFwSCv93POniN3n5l5Zp0d7jxz5xJRvNus/7WhXfNfTL7Pfh/WtLRTKDoN07C9zyRNWpZ2CkWi1bRnaadQJPI7JfNXxP4r0urFuzgvjJTW3m8OKgSjA5r/6MT7RlRWBUEQBEEQyhCJGAYgCIIgCIIgvLfK0MNRJUHMBiAIgiAIgiC8t0RlVRAEQRAEoQwRwwAEQRAEQRCE95cYBiAIgiAIgiAI7wdRWRUEQRAEQShLxDAAQRAEQRAE4X1Vlv5UakkQwwAEQRAEQRCE95aorAqCIAiCIJQlYhiAIAiCIAiC8N4SwwAEQRAEQRAE4f0gKquCIAiCIAhliOQDKzWKzqogCIIgCEJZ8oENAxCdVUEQBEEQhDLkQ/tzqx9YIVkQBEEQBEEoS0RlVRDeRKEo7QyKRL7979JOoUgkbbqVdgpF8vuwpqWdQpEM+/1YaadQZH9sn1naKfy/pkhPLu0UikSRHF/aKbx/xDAAQRAEQRAE4b0lhgEIgiAIgiAIwvtBVFYFQRAEQRDKEIkYBiAIgiAIgiC8t8QwAEEQBEEQBEF4P4jKqiAIgiAIQlkihgEIgiAIgiAI76sPbcyqGAYgCIIgCIIgvLdEZVUQBEEQBKEs+cAesBKdVUEQBEEQhDLkQxsGIDqrgiAIgiAIZckHVlkVY1YFQRAEQRCE95borApl1r1795BIJISGhgJw9OhRJBIJSUlJpZqXIAiCILxTEknJvMoIMQxAKFH9+/cnKSmJrVu3/ufb9vX1JSYmBmNj43e+LYVCwe9/rWDd1h2kpKZSy7MaE34cgXsll9cut+/wUX5bupyoR9E42tkyYvDXtG7WRPV+iy6f8Cjmcb7lPu3ehYk/jczXPmH6LNZt3UHA98Po3+eTIu2DxKsxkrqtwMAY4mOQH94Ij25rDrZzRdq0M5hVBG0dSElAcfkkiotHcmPcayFt0BZMLEGqBUlxKM4fQhF+rkh5Afy77xiB2w8Sl5SMm70NAf174uPhVmD8ufCbzFy1iciHMViZGjPg49b0btNELWbVrsME7T9OTHwipkb6tKlfh5GfdkZXpxwA6c8z+G3dDg6eu0xCcioeLvaM7d+TGm7ORc4fQNK4A9KW3cDIFGKikG1eBrfD37ygiwdaw6dDzH1kM4drXnedxmh9+RPysDPIl/38Vvm9LbfGvrT5cTiO3l6Y2NqwuEsfLm/b9Z/moMnaU5cJPHqRuNR03CqaM6ZzU3wq2WmMPXAlkqDgMK5Hx5GVI8PN2oyhbRrQqIrzu8vvZAiBh88Tl5KGm7UFY7q2wMfVXmNsXHIav247yrUHj7kfn0jfxt4EdGuhFpMtk7HswFm2nb/Kk+Q0XKzMGPlRUxp7vP4cVBCFQsHvgX+zfvsuUlLTqFmtKhNGfot7JefXLrfv6AkW/LWSqEcxONrZ8P3XX9K6aSONsUv/Xsu8pYF80bMrY4cPUe5HTg6//bmCY2fO8TD6MQb6FfD1qcPIwQOoaGFR6PzXHj5N4N4TxCWl4mZnxZg+nfCprPmziEtK4dd1u7l27xH3Y5/St2VDAj79SC3mwMWr/LnzKFGxT8mRyXCsaMGXbRvxsW+dQuf0LknEMABBKJt0dHSwtrb+TwaeL/v7X1b8u54Jo75n44o/sTAz48tvR5KW/qzAZUKuXGXE/ybTuX1btv0TSOf2bfl+7EQuX83twGxc8Scnd29RvVYsnAtAu5bN863v4LETXL4WgZVl4U/oL0mq1EHSogeKM/uQr5qO4mEk0h5DwdBU8wLZmSguHUO+dj7ywKkozuxF0ugjJDX9cmMyniE/sw/5mtnIV/2C4sppJO37grNHkXLbHXyBGSs34t+tHZtnBuDt4Yb/L38QHZ+gMf5hbDyDpi/C28ONzTMD+KZrO35ZsYH9Z0JUMTtOnGPuv1sZ2rMju+ZNYNqgvuw5fZG5/25TxfxvyT8Eh11n5rB+bJszDr+aHnw1dQFPEpKKlD+ApE4jpN0GIt+3HtnM4ShuX0Nr8CQwtXz9gnoV0Pp8BIqblwuOMbVE2uUrFJFXi5xXSdDV1+fh5asEDRtVKtvXZE/oDaZvP4Z/q3psGvEZ3pVs8f9rK9GJKRrjL9x5iG9lR5YM6MyG7/tQz9WBIYHbCX8U+27yu3Sd6VsO49+6AZtG9cO7kj3+SzcWmF9WjgxTg/L4t25AFVsrjTELdp1k/enLjO3eih1jvqKXby2+C9xK+MMnb5XjX2vWsXLdJsaPHMaGv37H0tyMr0aMJu3Za85pV8MZOXEaH7dtxbaVS/i4bStGTJjG5WsR+WKvRNxg/fbdVHGtpNaekZFJ+M1IhvTry6bARSz8eSL3HjxkyOgJhc59z7kwpq/dhX+n5mya9C3e7s74z1tJ9NMkjfFZOTJMDfXx79ScKg7WGmOM9Svg36k5/44bzJYpw+nWyJtxgZs4efVmofMSSo7orArvTLNmzfjuu+/46aefMDMzw9ramkmTJqnFTJo0CUdHR3R1dbG1teW7775TvSeRSPJVaE1MTFi5cqXG7eUdBrBy5UpMTEzYt28fHh4eGBgY0K5dO2JiYoq1XwqFgtVBGxj05ee0ad6Uyq6VmDlxLBkZmezcd6DA5VYFbcC3ng/+/fvi6uyEf/++NKjrzaqgDaoYM1MTLM3NVa8jJ4NxtLejXh0vtXU9iY1jyqz5zJ4ynnLaRb9BIvFpieLKaRRXgiHhCYojmyA1EYlXY80LxD5Ecf0iPI1RVlXDz8O9CLB/pdr54BbcugwJTyApHsWloxD3CImda5FyW7XzMN1a+NKzpR+u9jaM7d8TawsTgvYf1xgftP8ENhamjO3fE1d7G3q29KNb84YE7jioigm9eZc6VVzp1Kgudlbm+NWqRkc/H67duQ9ARlYWB86GMqpvF+pWc8fJ2ophn3TC3sqCtQVs93WkzbugOH0Axen98OQh8s1/QWI80kbtX79c76EoLh6Du9c1B0ikaPUbhXz3vyievl2npLiu7T3A9vFTCd2yo1S2r8nKY5foXs+THvWr41rRjIDOzbAxMSDodJjG+IDOzRjQ3IcajtY4W5oyooMfThYmHL12593kd/QC3evXoEfDmrhamxPQrQU2JoYEnQzVGG9nbszYbi3pXK86hnq6GmO2X7jGN63q07RaJRwsTOjdqDZ+VZxZeeR8kfNTKBSs3rCFQV/0oU3TxlSu5MKMcT+SkZnJzv2HC1xu9frN+Pp44/95Hyo5OeL/eR8aeNdm1frNanHpz54zavJ0pv40AiNDA7X3DA30CZw/k/Ytm1LJ0QGv6tX434hhXLtxi+jHhbt4WLnvBN0b+9CjSV1cba0I+PQjbMyMCTpyRmO8nYUpYz/9iM5+dTAsr6cxpl7VSrTy9sTV1gpHK3M+b+1HZXtrLt28V6ic3rkPbBiA6KwK79SqVavQ19fn7Nmz/Prrr0yZMoUDB5Qduo0bNzJv3jyWLl3KrVu32Lp1KzVq1CjR7T979ozZs2fz999/c/z4caKiohg1qngVoYfRMcQ9TaBR/bqqNh0dHerWrkXIlYKrXaFXrqktA9C4Qb0Cl8nKzmb73gN0/6iDWrVYLpfz46RpDOjb+43DDjSSaoG1A4p76tUPxb0IJHaVClgoDyt7sKuk7KAWxLEKmFZE8TCy0Kll5eRw7U4UfrXUq7F+NT0IuaG5IxF66y5+NfPEe1Xj2p37ZOfIAKhT1ZVrd6IIi7wHwIMn8RwPuUrTOtUBkMnkyORydMuVU1uPrk45Ll0vYGhEQbS0wcENxfUQtWbF9RAkLgVXmSX1WyKxsEG+Z22BMdL2vVGkJaM4U/BF0YcmK0dG+KNY/Co7qbX7VnYi9F7hLkzlcgXpmdkYV9DccSl2fg8f41fVWT2/qs6E3ntUrPXqllO/UNUrp82lO0Vf58Pox8Q9TcCvno+qTUdHh7peNQm5WvDQldCr4fjV81Zra1Tfh9A8y0yZu5BmvvXxrVu4W+ipaelIJBKMDPXfGJuVk0P4/Wj8PN3V2n093QmNjCrU9t5EoVBwOjySe4/j8KnydsMsSpxUUjKvMkKMWRXeqZo1azJx4kQA3N3d+f333zl06BCtW7cmKioKa2trWrVqRbly5XB0dKRevXoluv3s7GyWLFmCq6uyujds2DCmTJlSrHXGPX0KgLmZmVq7hZkZ0Y/zjzd9Kf5pAuZm6rfZzc1MiXuq+fb2wWMnSE1Lo2tH9WrcstX/oq2lxRe9erxN+lDeAIlUC9Lz3IJMTwV9o9cuKh00DcobgFQLRfAuZWX2VTp6SAf/ouywKeQoDqyD+wVUCTVISklDJpdjYWyo1m5ubER8kuZbpvFJKZgbq+dtYWxIjkxOYmoaVqbGdPTzITEllb7j56BAQY5MTu82jfm6S1sA9Mvr4VXZhcWb9uBqZ425iRG7Tp4nLPIeTtZvuHWfl74REi0tFKlJas2K1CQkRiaal7G0QfpxP2Tzx4BcrjnGxQNJg9YFjmP9UCWlP0cmV2BuWEGt3dywAvGpBd/CftWKYxd5npVNu1qV32F+6h0vc0N94lPS33q9jaq6sPLoBbxdHXA0N+HMrfscvhqJTK4o8rriEpTnIHMzE/UcTU2JflJwBT8+IRFz0zznNFNT4hISVT/vOniE8Ju32Ljsj0LlkpmZxZwlf9GpdQsM9N/cWU1KfYZMLsfcWL1ia25kQHxyaqG2WZDUZxk0+2E62Tk5SCVSxn/eGd88nWLhvyE6q8I7VbNmTbWfbWxsiI1V3trp2bMn8+fPp1KlSrRr144OHTrw0Ucfof0Wt7ULUqFCBVVHNe/2NcnMzCQzM1Ot7eCO3Uyd85vq56VzZwL576AoULzxtooE9fcVCkWBY2w3bd9Fk4b1qfjKmNSrETdYvW4jm1f/VfJjcyWA4vW/6ORr50E5XSS2zkiadIbEOOXwgJeyMpGvmg46ukgcqyBp3g1FcvzrK7Aac8nzOVHw56QhXLUbL9vPXbvJ0s37GD+wN7Xcnbn/OI7pKzawyGQ3Q3p0AGDmsP6MW/w3TQeNRUsqpZqLA538fAi/+6BouedNIjfLApKXotXvR+S7/4W4aM0xuuXR6vcD8qDf819kCED+T1ehKPATV7Mr5DqL9p9h4Zcf5+vwlqT8+b3+mH6TgG4tmBC0j06/LEciAQdzE7rWr86Ws28ey7xj/yEmzpqv+nnJr9Ne5JgvSw1t6vLvgkLVFvMkll9+W8TyuTPQ1dV5Y17ZOTmMnPQzCoWCiT98+8Z4tTzyZqEo/sT5+no6bJ70Lc8yszgTfptfg3bhYGlGvaqFvAP1Dok/CiAIJahcntuqEokE+YvKkYODAzdu3ODAgQMcPHiQIUOGMGvWLI4dO0a5cuWQSCQo8vzCz87OLvb2867zVdOnT2fy5MlqbWNHDmfr38tVP2e9yCH+aQJWrzyt+jQhEYs8ldNXWZibEZ+gXkVNSEzSuMyjmMcEn7/IwhlT1dovhF7maWIizTv3VLXJZDJmLljE6nUbObx1fYHbV3mehkIuy19FrWAIz95QiUhWVpUV8dFQwQiJX0f1zioKSIpT/iv2IZhXRFq/DfJCdlZNjAzQkkrzVVETklMxz1NtfcnCJH/V9WlKKtpaUkwMlNWWBet28HGTevRsqXwgrLKjHc8zMpn4578M6tYOqVSKo7Ulf08eybOMTNKeZ2BlasyIeX9hZ2VeqNxV0lNQyGRIjEx59UiTGBpDSlL+eL3ySJzckdpXgp6DXgRLkEilaM3finzRBBTpqUjMKyL9ZvwrK1T+stKavxXZtEEQX3BV//8zE/3yaEkl+aqoCWnP3tj53BN6g/HrDzLv8474VnZ8x/mpV1ELk9/rmBlU4PeBXcnMziEp/TlWxgbM3XEcO/M3z4bSvFFDalarqvo5K+vFOS0hESuL3OP9aWJSvrtBr7IwMyX+lSrqy2UsXlRbr924xdPEJLoPHKJ6XyaTc+HyFdZs3kbY4d1oaWkByo7qiPHTeBj9mJULZhWqqgpgYlhBec5ITlNrT0hNw9zIoIClCkcqleJUUXmO93C05U5MLMt2HX0vOqtl6RZ+SRCdVaFUlS9fno8//piPP/6YoUOHUrVqVa5cuUKdOnWwtLRUexjq1q1bPHvNk6klISAggJEj1aeI0n2ehK5u7kMOCoUCS3MzTp27QLUqytuGWdnZnA+5zKih/gWu26uGJ6fOnlebYurk2fPUrlE9X+zmnbsxNzWhmV9DtfbOHdri+8q4MoABw0fRuX0bunXqULidlMvg8QMkTlVR3Mp96lziVBVFpOYHUjSSoLzd/6agN8bk0tHWxrOSI8FhEbSu56VqDw67Tou6NTUu4+XuwtGLV9TaTl2OwLOSE+W0lb8In2dm5atEaEmlKBSQ99Klgp4uFfR0SU57xqnLEYzq27XQ+QMgy4EHkUiq1kYRlvuAh6SKF4orZ/PHZzwj55ehak3Sxh2hck1ky6fD0ycgl+eP6fQ56JZHvulPSIwvWo7/j+hoa1HNzorgm1G0qpH7wF/wzShaVC+4U7Er5Dr/W3eAWX3b07TauxuHqKOtRTV7a4Jv3KdVzdxhBsE37tOiesHTsRWWbjltKpoYki2TsT/sJu28qrxxGYMKFTCokNtRfnlOCz5/kWqVlTllZWdzPjSMHwYNLHA9XtWrEXz+Iv17dVe1nTp3Ea/q1QBo4FOb7av/VFtm7C+zqeTkwMDPeuXrqN5/+IhVC2Zhavz64Uiv0tHWppqTLcHht2jl7alqD74WSYvaRZuJ5E0UCuUYWeG/JzqrQqlZuXIlMpmM+vXrU6FCBf7++2/Kly+Pk5PyQYkWLVrw+++/06BBA+RyOaNHj85XKS1purq6ah1TAOTP1X6USCR80bsnS1f+g7ODPU4O9ixd+Q96erp0attaFffTpJ+paGnBDy86sF/06kHfQd/x5+o1tGzSiEPHT3L63AX+/VN9LJdcLmfzzj106dgu35AIU2NjTPPMI1tOWxsLMzMqORW+MqS4cAhJx37wOApF9B0ktRqBkRmKyyeV+9j4YzA0QbF7tfLn2k1QpCQoO06AxN4VSd1Wyif+X34u9dugeBylrKxqaSOp5InEsz6KA0GFzgugX6cWjFm4iuqVnPCq7ML6g6eIiU+kV2vlTAVz/93Kk4QkZg7rD0DvNo35d98xZqzaSM+WfoTevMvmw8HMHv6Vap3NvWuwctdhPFwcVMMAFqzbSXOfGmhJlc+ZngwNR4ECF9uK3H8cx+y/t+BiW5GuzRrmy/FN5Ee2Iv18JJKoWyjuXkfq1w7MLJGf3AOA9KMvwMQc+d/zlL8BY/I8CJKaBNlZ6u15Y56na25/x3T19bF0y+0EWrg4Y1+rBukJiSQ+ePif5vJS/6Z1GL12H54OFfFysmHDmSvEJKXSq4HyAmfu7pPEJqczo49yjPKukOsErN1PQOem1HK0Ie7F2FG9ctoYltf89H2x8mvmw+g1u/B0sMbL2ZYNpy8Tk5hCL79ayvx2HCc2OZUZfTuqlol4MQXVs6wsEtKfEfHwCeW0tXCzVlb6Lt+LJjY5jap2VjxJTuOPvadQKBQMaFH0cf8SiYQvenZl6d9rcbK3w8nBjqWr16Knq0unNrnzu46eOhMrSwt+GDQAgM97duXzYSNZ9k8QLRv7cuhEMKcvXGLNonmAslNcOc9DoOX19DAxMlK15+TIGP6/KYTfjGTJzKnI5HLVOH5jI0N0CnHO79+2MaOXrcfT2R4vV0c2HDtHTEISvZrVV36+G/cSm5jCjK9zCwURUcohN88yskhISyciKppyWlq42VUE4M9dR6nubIeDpTnZshyOh91g++lLTPi8S5E/33dCDAMQhP+GiYkJM2bMYOTIkchkMmrUqMGOHTswN1fehpozZw5ffvklTZo0wdbWlt9++42LFy++Ya3/ja8//5TMzEwm/zqX5NQ0anl6ELhgDgb6udWKmCdPkL5yq6ZOzRrMnTqR+Uv/YsHS5TjY2zLv50nUelGFeCn43AWiHz+h+0cdeVcUNy5BeX0kvu2R6Bsp/yjApkWQ8mKYgoExEsNXb2NLkDbuDMbmoJArJ/w/vg1F6MnclZbTQdq6FxiYQE62ckqsXSuV2yqCDr4+JKWms2jTbuISU3B3sGFJwBDsLJXHRVxiCjHxubce7a0sWBIwhBmrNvHvvuNYmRoz9suetGlQWxUzqHt7JBIJC4J28CQhCTMjA5p51+D7Ph+rYlKfPWfe2m08fpqEsUEF2tSvzfd9PlZVZ4tCcekkcn0jpO16g5GZcoL/xZMhUTlEAmMzJG+ac/U95eRTm5FHd6t+7jlvOgCnV65h1ZeDSyWn9l5VSErPYPGBM8SlPMPd2pylAzpjZ6as0MWnpBPzypym609fIUcuZ+qWI0zdkvuHLbr4ePBL77Yln1+dqiQ9e87ifcHEpaTjbmPBUv/u2JkZv8gvjZhE9SE43WevVv372oMn7LoYga2pEQcnKi9+s3Jk/Lb7JA+fJlFBV4cmHi7M7NsRo7ec0WDgZ73IyMxiytyFJKemUrNaVZbPm6FWgY1+Eqs2GX2dGp7MmTSO35atZMFfq3Cws2HulHHU8ix8RfNxXByHT54GoMuXg9TeW7VgNvXr1HrjOtrXq0lSWjqLtx8iLjkVd7uKLP2+P3YWyuEI8cmpxOSZL7n7pIWqf1+7/4hdZy5ja27CwVmjAeXdmCl/b+NJYjK6OuWoZG3JzK970b6e5js8/7kPrLMqUbxuAJ8gCJBUOvNZvi3ZsuLNdvBfk7TpVtopFIn8r/mlnUKRDPv9WGmnUGR/bJ9Z2ikUjfa7veNT0qQ+bUo7hSKR37xQ2ikUiZbfuz+n5QzvXCLr0f5t25uD3gNinlVBEARBEAThvSWGAQiCIAiCIJQl0g+r1ig6q4IgCIIgCGXJBzZm9cPqmguCIAiCIAhliqisCoIgCIIglCWisioIgiAIgiC8tySSknm9hUWLFuHi4oKenh7e3t6cOHGiUMudOnUKbW1tvLy8irxN0VkVBEEQBEEQ3mjdunV8//33jBs3jpCQEBo3bkz79u2Jinr9HydJTk7miy++oGXLlm+1XdFZFQRBEARBKEuk0pJ5FdHcuXMZMGAAAwcOxMPDg/nz5+Pg4MDixYtfu5y/vz+ffvopDRsW/S8CguisCoIgCIIglC0lNAwgMzOTlJQUtVdmZqbGTWZlZXHx4kXatFH/oxJt2rQhODi4wFRXrFjB7du3mThx4lvvruisCoIgCIIgfICmT5+OsbGx2mv69OkaY+Pj45HJZFSsWFGtvWLFijx+/FjjMrdu3WLMmDGsWbMGbe23f6ZfzAYgCIIgCIJQlpTQbAABAQGMHDlSrU1XV/cNm1bftkKhyNcGIJPJ+PTTT5k8eTKVK1cuVp6isyoIgiAIglCWlFBnVVdX942d05csLCzQ0tLKV0WNjY3NV20FSE1N5cKFC4SEhDBs2DAA5HI5CoUCbW1t9u/fT4sWLQq1bdFZFQRBEARBKEtK4c+t6ujo4O3tzYEDB+jatauq/cCBA3Tu3DlfvJGREVeuXFFrW7RoEYcPH2bjxo24uLgUetuisyoIgiAIgiC80ciRI/n888/x8fGhYcOG/Pnnn0RFRTFo0CBAOazg0aNHrF69GqlUSvXq1dWWt7KyQk9PL1/7m4jOqiAIgiAIQllSSn/BqlevXjx9+pQpU6YQExND9erV2b17N05OTgDExMS8cc7VtyE6q4IgCIIgCGVJKf651SFDhjBkyBCN761cufK1y06aNIlJkyYVeZuisyoIb6BIiS/tFIrGxb20MygSxdnDpZ1C0RgYlHYGRfLH9pmlnUKRDf14dGmnUCR/HF9e2ikUTVpCaWdQNJfPlnYGRePXrbQz+H9HdFYFQRAEQRDKklKsrJYG0VkVBEEQBEEoQySlMBtAafqw9lYQBEEQBEEoU0RlVRAEQRAEoSwRwwAEQRAEQRCE99YH1lkVwwAEQRAEQRCE95aorAqCIAiCIJQlH1hlVXRWBUEQBEEQypIPbDYA0VkVBEEQBEEoSz6wyuqH1TUXBEEQBEEQyhRRWRUEQRAEQShLPrDKquisCoIgCIIglCUfWGdVDAMQBEEQBEEQ3luisiq8t/r378+qVatUP5uZmVG3bl1+/fVXatasCYDkxdXl6dOnadCggSo2MzMTW1tbEhISOHLkCM2aNVPFb9myhS5duhQrt3+372H5hm3EPU3EzdmBsYO/wqdGtQLjz12+xoylK4i89wArczMGftKF3h+1Vb1/614UC1YFce3WbaKfxBEw+Ev6dftIbR05Mhm/r17HjsPHiU9IwtLMlK5tmjP4sx5I3+LJ0LVnrhJ4MpS41Ge4WZkypqMfPs62GmMPXLtD0NlrXI+JJ0smw83KjKEtfWjk7qiK2XA+nG0hN4h8kgBANTtLvm9dn5oOFYucm8Z8Q28TeP4GcekZuJkbMaZ5LXzsLTXne+sRQaG3uR6XRJZMjpu5EUN9q9HI2VotbvXFWwRdvk1M6jNM9XRpU9mOEY1roKutVex8JQ1aI23cCQxNIPYhsp2r4d4NzcFOVdBq1wesbKGcLiTGIT93CMWpPbkxUi0kzTojrdMEjEwhPgb53rUobl4udq6arD11mcCjF4lLTcetojljOjfFp5KdxtgDVyIJCg7jenQcWTky3KzNGNqmAY2qOL+T3IrCrbEvbX4cjqO3Fya2Nizu0ofL23b953msPXKWwH0niEtKw83WijG9O+BT2VljbFxSKr+u38O1+9Hcj31K35YNCOjdscB17z4Xxqg/19PCy4Pfh332Vvn9u2MfyzfuIC4hCTcne8YO6odPdY8C48+FhTPjz9VE3n+IlbkpA3t+TO+OrVXv7z95lqXrthIV/ZicHBlOdtZ82a0TnVs1UVvPk/gEZi9fw/ELoWRmZeFsZ8O0EYOo7l6pSPmvvXyHwEuRL84PhoxpUgMfOwuNsQciowkKu8v1+GTl+cHMkKENqtLIKfdclS2Ts+zCTbZFRPEkLQMXUwNG+nnS2LlkzmfF9oHNBvBh7a1Q5rRr146YmBhiYmI4dOgQ2tradOrUSS3GwcGBFStWqLVt2bIFAwODd5LT7qMnmb54BYP6dGfL4jn4VPfgm7HTiI6N0xj/MOYJ/v+bhk91D7YsnoN/n278vGg5+06cVsVkZGbiYFORHwZ8jqWZicb1/BW0haCd+xg/bCC7li9g1Nefs3zDVv7ZurvI+7AnLJLpu0/h37QOm4b2xNvZBv9Vu4hOStUYf+FeNL5u9izp15ENQ3pQr5ItQ/7eQ3h07j6fuxtNx5rurBjQmX8HdcPG2JCvV+7kSXJakfPLl+/1B0w/Eop/fQ82fd4Kb3sL/DefJDrlmeZ8H8bh61SRJd0asaFvS+o5WDJkyynCnySqYnZERDH3xBWGNKzGzv5tmdrWmz03HjLvxJVi5yup0QBpxy+QH9mKbGEAins30Oo/BozNNS+QlYn8zH5kS6cgm/sD8iNbkbb5BEndFqoQaZtPkNZriXzHSmTzfkR+9iDSviPBxrnY+ea1J/QG07cfw79VPTaN+AzvSrb4/7WV6MQUjfEX7jzEt7IjSwZ0ZsP3fajn6sCQwO2EP4ot8dyKSldfn4eXrxI0bFSp5bDn3BWmB+3Gv0MzNk0YgndlJ/x/W0300ySN8Vk5OZga6uPfsSlV7K01xrz06Gkiszbsxdvd6a3z230smOlLVzGod1e2/DEDn+pV+eZ/04mOjdcY//BxLP7jlXFb/piBf68u/Lx4BftOnlXFGBsaMKh3V4LmTWXb4l/p1qYZY+cu5sSFUFVMcmoafUZOQFtbi2XTAti5dA6jv/4cI/0KRcp/z82HTD9+Bf+6ldn0aXO8bc3x33a64PPDo3h8Ha1Y8nFDNvRuRj17S4ZsP0N4bJIqZsHpCNZfucfYpjXZ8XlLetVw4budZ9ViSpVEUjKvMkJ0VoX3mq6uLtbW1lhbW+Pl5cXo0aN58OABcXG5naR+/foRFBTE8+fPVW2BgYH069fvneS0ctMOurdrSc8OrXF1smfskAFYW5qzdsc+jfFBO/dhY2nB2CEDcHWyp2eH1nRr24LADdtUMTWquPPTN/3o2LwR5cqV07iekIgbtPStR7P6PthbW9GuiS9+3l5cvXm76Ptw6jLdvavSo241XK1MCejYCBtjA4LOXtMYH9CxEQOa1KaGvRXOFiaMaNMAJ3Njjl6/r4qZ9Ukr+jSojoetBZUsTZnStSlyhYIzdx4VOb98+V68SfcaLvSo6YKruREBzb2wMaxA0GXN+x7Q3IsB9apQw9oMZ1NDRjSugZOpIUfvxKhiLkc/pbadOZ08HLEz1sfP2ZoOVR24+kqH9m1JG3dEceEIigtHIC4a+c7VkPwUaYPWmheIuYficjDEPoSkeBShJ1HcDEPiUlUVIqndGPnRrShuhEJiLIqzB1HcvIy0ccEVt7e18tglutfzpEf96rhWNCOgczNsTAwIOh2mMT6gczMGNPehhqM1zpamjOjgh5OFCUev3Snx3Irq2t4DbB8/ldAtO0oth5UHTtG9kTc9mvjgamtFQO+O2JgaE3T0nMZ4OwtTxvbpSGff2hiW1y1wvTK5nNHLNjDs4xY4WJq9fX6bd9G9bQt6tm+Jq6M9Ywf1V57Tdu7XGB+06wA2VuaMHdQfV0d7erZvSbc2zQncmPsZ16/lSWu/erg62uNoa80XXTpQxcWRS9dy7y78tWE7NpbmTP9hCDWruGFvbUXD2jVwtH19Bz1f/pdu093TiR7VnXE1MySgaU1sDMoTdOWuxviApjUZ4ONODWtTnE0NGOFXDScTA47efayK2X79Ad/UrUxTF2scjPXpXdMFPycrVl6KLFJuQskQnVWhzEhLS2PNmjW4ublhbp5bofL29sbFxYVNmzYB8ODBA44fP87nn39e4jlkZWdz7eZt/LxrqbX7eXsRcu26xmVCI27i5+2l1tbIx4trN2+TnZNT6G17V/fgdEgYdx9GA3D99l0uXY2gSb06RduHHBnh0XH4uTmotfu6ORAa9biApdTJ5QrSM7Mxfs0v0ozsHHJk8tfGFCpfmZzwJ0n4OanffvN1qkho9NPC5atQkJ6VjbGejqqtjp0F4U+SCItRDlt4kJTGibuPaepiU6x80dICWxcUt9Q7dopbYUgcKxduHTbOSJwqo7gTkdumrQ052epxOdlInKsUL988snJkhD+Kxa+yeqXOt7ITofdiClhKner4qKBXormVRVk5OYTfj8bP002t3dfTjdDbUcVa96IdRzA11Kd7Y5+3zy87h2u37uBXp6Zau1+dWoRE3NS4TGjETfzqqJ8DG3nX4tqtOxrPaQqFgtMhV7j7MAafGrlDCw6fuUD1ypUYPm0uvr2+puvQ0azfc6ho+cvkhMcm4edopdbu62RF6Ivv9psozw85aueHLJkMXS31LpKethaXCnnOeec+sMqqGLMqvNd27typup2fnp6OjY0NO3fuzDdG88svvyQwMJC+ffuyYsUKOnTogKWl5vGMxZGYnIpMLsfc1ESt3dzUmPjEJI3LxCUk0sjHK0+8CTkyGYnJKViZF64i8nWvrqSmP6PDV9+iJZUik8v5/stP6dSicZH2IelZBjK5AnMD9Vtt5gbliU/TfNssrxWnQnmelU27Gq4FxszddwYrI30autoXKb98+T7PRKZQYF5BvdNrrq9L/L2MwuV74SbPs2W0q5KbS4eqDiQ8y6Rv0BEAcuQKeteqxNf1qxa0msKpYIRESwtFWrJasyItGYmh8WsX1RrzO+gbgVQL+aGNysrsy+VvhiFt1BHZ3euQ8ASJa3UkHt4lPnYtKf258vgwzHN8GFYgPrWQx8exi8rjo1YhO+f/jyWlPVOeM4zUhyWZG+kTX4whMpdu3WfzyYtsnjC0WPklpqS8OKepH5vmpsbEJyRpXCYuMZlGGuKV57RUrMxNAUhNf0bTzwaRlZ2DVCpl4rABap3iBzGxrN15gP7dOuLfuythNyL5efEKdMpp06VV00LlX+D5obwu8emZhVrHikuRPM/JoZ177pjsRo4VWRlyG287CxxN9DkTFcfhO4+RKRSFWuc794GNWRWdVeG91rx5cxYvXgxAQkICixYton379pw7dw4np9zKT9++fRkzZgx37txh5cqVLFiw4K22l5mZSWam+glOJzMLXV0dtTZJ3itShYa218YrNLe/xu6jp9hx6BizA0bg5uzA9ci7/LI4ECtzM7q2aV7o9eTmlD8lCW/OZ9flWyw6dIGFfdvn6/C+tPx4CLvCIlk1sDO65UrmNJP3syp0vhFRLAoOZ2EXX8xfqfSdexDL0rMRTGhZh5o2ZkQlpfHLkVAsT4czuGHBD8u9PYnq/70gsqWTQUcPiaM70na9kT99ohweAMh3rkLa9Wu0Rs5RrifhCYqLx5B4F+6X+ltkq0b5eb/ZrpDrLNp/hoVffpyvw/sh0/h9e8vCVnpGJqOXb2DyF10wNdQvfnJo+C4pFK8/p+Vt0HBO0y+vx5ZFv/LseQanQ68w48/V2FtbUb+W54tF5Hi6uzLyyz4AVHNzIfL+Q9buPFDozqoqn7znBwr3+e668ZBFZ66z8KP6ah3egKY1mHAohE5/H0SCBAdjfbpWc2RLePGq4cLbEZ1V4b2mr6+Pm1vu7TNvb2+MjY1ZtmwZ06ZNU7Wbm5vTqVMnBgwYQEZGBu3btyc1VfPDQq8zffp0Jk+erNY24fvBTBqhrF6YGhuiJZUSn6A+rvFpUjLmJpqrZpZmpvkqFE+TktHW0sLEyLDQuc1atoqve3WjY/NGAFRxcSI6No4/gzYXqbNqUkEPLakkX5UsIf055gblX7vsnrBIxm85yrzebfB101wxDTwRyp/HLrH8y4+oYl3AA0VFYFJeFy2JhPh09SpqwrNMzPVfP8Rgz/UHjN9/kXkfNcA3zzCCBaeu8XE1J3rUdAGgsqUxz7JzmHTgEv4NPJC+bU/iWQoKmQyJgTGvdk0lBkaQpvkBJZVE5VhsxZMHyA2MkbbsjuxFZ5X0VOT/zAXtclDBAFISkbbro1qmpJjol9d8fKQ9e2Pnc0/oDcavP8i8zzviW9nxtbEfChODCspzRp4qakJqer5qa2FFxSbwKD6JoQv/UbXJX3QWa3wzgV3ThuNoVbjvnqmRkTK/PHeGnial5Ku2vmRpakx8YnK+eOU5LXefpFIpTi/Gn3q4OnMn6hF/rtuq6qxampni5qg+w4Srox37T52lsAo8PzzPzFdtzWvPzYeMPxjCvA518c0zjMCsgi6/f9SAzBwZSRlZWOnrMfdUOHZG78kFWBm6hV8SPqw6slDmSSQSpFKp2sNUL3311VccPXqUL774Ai2tt5t6KCAggOTkZLVXwJCvVe/rlCuHZ2VXgi+pTxcUfOkytT013z728qicL/7Uxct4VnalnHbhrxefZ2QilaqfoKRSKXK5vNDrANDR1qKarSXBkQ/V2oMjH+LlWPCDDbsu32LspsP8+kkrmlbV/OTx8hMhLDlykT/7daS6vZXGmKLS0ZJSraIJwfefqOd7/wletgX/Qt4VEcXYfef5tUM9mlbKPw41I1tGno8TLYkEBYo3FUBfTyaD6LtI3NXHAErcaqCI0jwGUCMJyo5pXjnZkJKonMqqej0U4ReKkWx+OtpaVLOzIvimegUp+GYUXs4Fj+fdFXKdsUH7+fWzdjSt5lKiOZVlOtraVHOyJThc/cGc4PBIvFzfrkNfycaCbZO/ZfPEoapX81pVqVfFhc0Th2Jt9vrhJmr5ldPG070SwSHqY6yDQ8Ko7aF5GIeXR+V88acuheHpXum15zSFQjlG9qXa1apw96H6OOh7j2KwtSr8EC4dLSnVrEwIjlK/aAuOisPLpuAhVrtuPGTs/kv82s6bpi4Fn/d0tbWoaFCeHLmC/ZHRtNBwLikVYsyqILw/MjMzefxY+dBPYmIiv//+O2lpaXz00Uf5Ytu1a0dcXBxGRkZvvT1dXV10ddWvxhVJ6kMA+nf/iNEzF1C9shteHlVYv3s/MbHx9O7UBoA5y/8hNv4pM0cPB6B3p7as2b6H6UtW8En71oRG3GDT3kPMHjtCtc6s7Gxu31d2HrOzc3gSn0BE5F0qlNfDyU55cmzeoC5L/t2IjZUFbk6ORETeUc5M0LYFRdXfrxajNx7C084SL0drNpwPJyY5lV71lBWPufvOEJuSzoyeLQFlRzVg42ECOvpRy6EicS+qbnrltDDUU35ey4+HsODgOWZ90gpbUyNVTAWdcujrap7hoND5eldm9J5zeFY0xcvWnA1hd4hJfUavWsq5GOeeuEJs2nNmtK+nzDciioC95wlo7kUtW3PiXlRd9LS1MHyRSzNXG1ZdvIWHlalyGEBiGguCr9G8ki1aeXuxRSQ/sQvpJ0ORPLyDIuom0notwcQC+dmDAEjb9gYjU+QblENcJA1aQ9JTFHHKh+ckzlWQNu6EIviVGSYcXJEYmaGIvg/Gpkhb9gCJBPnxkn/KvX/TOoxeuw9Ph4p4Odmw4cwVYpJS6dVA2QGfu/skscnpzOijnCt4V8h1AtbuJ6BzU2o52hCXkg6AXjnt1z7N/l/Q1dfH0i13zk4LF2fsa9UgPSGRxAcPX7Nkyenf2o/Ryzfi6WyHVyUHNhy/QExCMr2a1QVg7qb9xCalMGNAD9UyEVHKTtyzzCwSUtOJiIqhnLYWbrZW6JYrh7ud+p0CoxdDXPK2Fyq/bh0ZPet3qru74uXhzvo9h5TntBfzps4J/JfYpwnM/HEYAL07tmbN9n1MX7qaT9q3IDTiFpv2HWb2mOGqdS4N2kL1yq442lQkOyeHY+dC2HboOBOHDcjdbtcO9Bk5gSVBW2jfpCFhNyJZv/sQU4Z/TVH0r+PK6H0X8axogpeNGRuu3FOeH2ooL5rmnrpGbFoGM9p6A8qOasD+iwQ0qUEtazON54fLjxOITcugqqUxT9Ke88eZ6ygUCgb4uGlO4r9WhjqaJUF0VoX32t69e7GxUXbWDA0NqVq1Khs2bFBN8v8qiUSChYXmSaBLUodmjUhKSeWPf9YTl5CIu7MjS38eh11FZSUx7mmi2vyE9jYVWTrtf8xYEsi/2/dgZW7GuCEDaNu4oSom9mkiXQf/oPo5cMM2Ajdso25NT/6eMxWA/w0byIKV/zJlwZ88TUrBytyUXh3bMKRvzyLvQ/uabiQ9y2DxEeWk7+4VzVj6RUfsTJXDEuJTnxHzym3L9efDyZHLmbrjBFN3nFC1d6ldhV96KDvLa89eI1sm5/u16tPdDGnhw7CWdYuco1q+VR1Iyshi8ZkI4tIzcDc3Ymm3RtgZKcfrxadnEPPKnIrrw+6QI1cw9VAIUw+F5Obr6cQv7ZS5DGrggQQJv526Smzac0zL69K8ki3DG3kWK1cAxZUzyPUNkbbspvyjAE8eIFs5E5JeHBeGJkhMXjlWJVJlB9bMEuRyePpEOeH/uVeejNbWQdr6EzCzgqxMFDdCkK1fBBmFe+ipKNp7VSEpPYPFB84Ql/IMd2tzlg7ojJ2Z8kIwPiWdmFfmXF1/+ory+NhyhKlbch8K6+LjwS+92+Zb/3/Jyac2I4/mzkXcc950AE6vXMOqLwf/Jzm0r1eDpPRnLN5xhLjkVNxtK7J0+OfYvXgQKT45lZg8c652n/KH6t/X7kez62wYtuYmHJxZ8vPFdmjqqzynrdlEXGIi7k4OLJ06BruKygpnXEIS0bG5T8HbW1uxdOoYZixdxb8792FlZsq4wV/StlF9VczzjEym/L6cx/FP0dPRwcXBjl9/GkaHpr6qmBpV3Fg44QfmrljLojWbsLe2JGBQPz4q4kOj7Svbk/Q8i8VnrxP3LBN3c0OWdm6oumUfn55BzCvDWtZfuas8PxwNY+rR3ApxFw8Hfmmj7NBm5cj57XQED5PTqVBOmybOFZnZ1hujPM8vCP8NiULxvjzaJgjvJ0WU5rlH31fycwdKO4WiSSjZMZfvmuJu6c8dWhQS3yZvDnrPDP14dGmnUCR/HF9e2ikUidTevbRTKBL5nrWlnUKRaA2Z+c63IVv4w5uDCkHr2zklsp53TVRWBUEQBEEQypIPbBiAeMBKEARBEARBeG+JyqogCIIgCEJZ8oFVVkVnVRAEQRAEoSyRfFg3xj+svRUEQRAEQRDKFFFZFQRBEARBKEuKORd0WSM6q4IgCIIgCGWJGAYgCIIgCIIgCO8HUVkVBEEQBEEoS8RsAIIgCIIgCMJ7S/ph3RgXnVVBEARBEISy5AOrrH5YXXNBEARBEAShTBGVVUEQBEEQhLLkA5sNQHRWBUEQBEEQyhIxDEAQBEEQBEEQ3g+isioIgiAIglCWiNkABEFQo6df2hkUjbV9aWdQJNLaTUo7hSKR37xU2in8v/fH8eWlnUKRDG0yoLRTKJLFd0+UdgpF41q1tDN4/4hhAIIgCIIgCILwfhCVVUEQBEEQhLJEzAYgCIIgCIIgvLekYhiAIAiCIAiCILwXRGVVEARBEAShLBHDAARBEARBEIT31gc2G4DorAqCIAiCIJQlH1hl9cPaW0EQBEEQBKFMEZVVQRAEQRCEsuQDmw1AdFYFQRAEQRDKkg9szKoYBiAIgiAIgiC8t0RlVRAEQRAEoSwRD1gVn0QiYevWrYWOnzRpEl5eXu8ilfdS3v3t378/Xbp0KbV8yoIP7RgRBEEQhAJJJSXzKiOKVFnt378/q1atUi6orY2ZmRk1a9akT58+9O/fH6lU2feNiYnB1NS05LN9jXv37uHi4kJISEiJdmqcnZ25f/8+AOXLl6dSpUp8++23+Pv7l9g2fvvtNxQKRYmtrziOHj1K8+bN87WPGzeOadOm/Sc5SCQStmzZotaBHzVqFN9+++1/sv3CUCgU/L7iH9Zv301Kaho1q1VlwsihuLs4v3a5fUdPsOCv1URFx+Boa8P33/SndRM/1ftrt+xg7dZdPHr8BAA3FyeG9v+MJg3qalzfhFm/sX77bgK+9affJ92KtA9rD58hcN9J4pJScbOzYkzvjvhU1px/XFIKv67fw7V70dyPfUrflg0J6NOxwHXvPhvGqD/X0cLLg9+/7VukvAD+3bmf5Zt2EpeQhJuTPWO/+QKf6lULjD93JZwZy/4h8v5DrMxNGdi9E707ttYYu+tYMD/MXEjLBj78MeEHVfv5KxEs37STa5F3iEtI4vf/jaSVr+bPvTDWngwh8PB54lLScLO2YEzXFvi42muMjUtO49dtR7n24DH34xPp29ibgG4t8sWtPnqBoFOhxCSlYqpfnja1KjOiUxN0yxX/JllJ55stk7HswFm2nb/Kk+Q0XKzMGPlRUxp7uBQ7V4C1R84SuO8EcUlpuNlaMaZ3h9ccv6nK4/f+y+O3AQG9X3P8ngtj1J/rlcfvsM9KJN/CcmvsS5sfh+Po7YWJrQ2Lu/Th8rZd73y7/+7Yx/IN23O/c4P641PDo8D4c2HhzFi6Kvc71/Njendqo3p//8mzLA3aQlT0Y3JyZDjZWfNl94/o3KqJxvUtDdrCvBVr+aJLB8YO7l/k/NeeuETgobO5x2/3Vvi4OmiMjUtO49eth5XHb1wCfZv4ENC9lVpMvwVrOB/5IN+yTaq5smRQzyLn9//JokWLmDVrFjExMXh6ejJ//nwaN26sMXbz5s0sXryY0NBQMjMz8fT0ZNKkSbRt27ZI2yxyZbVdu3bExMRw79499uzZQ/PmzRk+fDidOnUiJycHAGtra3R1dYu66vfWlClTiImJISwsjC5dujBo0CDWrVtXYus3NjbGxMSkWOvIysoqmWReuHHjBjExMarXmDFjSnT9RWVgYIC5uXmp5vCqv/5dz8p1mxk/Yigbli3E0syUr0YEkPbsWYHLhFwNZ+SkX/i4bUu2rVjEx21bMmLCz1y+dl0VU9HKkh8GfcXGZQvZuGwhDerUYmjAJG7dvZdvfQePBxMWfh0ri6J/LnvOhTE9aDf+HZuyaeJQvN2d8Z+/iuinSRrjs3JkmBro49+pGVXsrV+77kfxiczasAdvd+ci5wWw+9hppv+5mkG9urBl4XR8PKvwzYQZRMfGa4x/+DgW/wm/4uNZhS0Lp+P/SWd+XrqKfSfP5s/tSRy//rUGH8/8Hd/nGZlUdXFk/OAv3yrvV+25dJ3pWw7j37oBm0b1w7uSPf5LNxKdmKIxXvn5lse/dQOq2FppjNlxIZy5O48zpJ0vO8d8xdTebdkTcp15O4+/l/ku2HWS9acvM7Z7K3aM+YpevrX4LnAr4Q+fFD/fc1eUx2+HZmyaMATvyk74/7b6NcdvDqaG+vh3bPrm4/dpIrM27MXb3anYeb4NXX19Hl6+StCwUf/ZNncfDWb6kpUM6tONLYtm4lPdg2/+98vrv3P/m45PdQ+2LJqJf++u/Lx4BftOnFHFGBsaMKhPN4LmT2Pbkll0a9OcsXMWceJCaL71XbkRyfrdB6ni8naf+Z5LEUzffBD/Nr5s+ulLvF0d8F+8nuiEZI3xWTk5yuO3TcMCj9/fBnTj2LRhqte2gAFoSSW0rV3lrXIscRJpybyKaN26dXz//feMGzeOkJAQGjduTPv27YmKitIYf/z4cVq3bs3u3bu5ePEizZs356OPPiIkJKRI2y1yprq6ulhbW2NnZ0edOnUYO3Ys27ZtY8+ePaxcuRLIPwxg9OjRVK5cmQoVKlCpUiXGjx9PdnZ2vnUvXboUBwcHKlSoQM+ePUlKSlJ7f8WKFXh4eKCnp0fVqlVZtGiR6j0XF+XVeu3atZFIJDRr1qxQy2VlZTFs2DBsbGzQ09PD2dmZ6dOnq23X0NAQa2tr3NzcmDZtGu7u7qr9S05O5ptvvsHKygojIyNatGjB5cuX1ZafMWMGFStWxNDQkAEDBpCRkaH2ft5hAKmpqXz22Wfo6+tjY2PDvHnzaNasGd9//70qxtnZmWnTptG/f3+MjY35+uuvAQgODqZJkyaUL18eBwcHvvvuO9LT09X296effsLOzg59fX3q16/P0aNH8/1fWFlZYW1trXoZGBhw9OhRJBKJ2v9LaGgoEomEe/fuAbBy5UpMTEzYt28fHh4eGBgYqC5wXhUYGIinpye6urrY2NgwbNgw1X4BdO3aFYlEovo57zAAuVzOlClTsLe3R1dXFy8vL/bu3at6/969e0gkEjZv3kzz5s2pUKECtWrV4vTp0/n2tagUCgWr129l0Be9adO0EZUrOTNj3CgyMjPZeeBIgcut3rAFX586+H/em0pOjvh/3psG3l6s2rBFFdPCrwFNG9bDxdEeF0d7RnzzJRXK66l1aAGexMUzdf4fzJowGm3tolfVVu4/RffG3vRoUhdXWysC+nTExsyYoKP5O3gAdhamjP20E519a2NYQa/A9crkckYv28Cwzi1xsHy7uysrt+yie5vm9GzXAldHO8b698Pa0py1uw5ojA/afRAbK3PG+vfD1dGOnu1a0K11MwI3q1ejZDI5P876g2/79sDeJv8vqCZ1vfi+Xy/a+NV7q7zV9uHoBbrXr0GPhjVxtTYnoFsLbEwMCToZqjHeztyYsd1a0rledQz1NF/oX74XTW0XOzp5V8PO3Bi/qi50qOPB1QeP38t8t1+4xjet6tO0WiUcLEzo3ag2flWcWXnkfPHzPXCK7o286dHER3n89u6IjakxQUfPac7XwpSxfToqj9/yBRdSVMfvxy1wsDQrdp5v49reA2wfP5XQLTv+s22u3LyT7m1b0LN9S1wd7Rk7uD/Wlhas3blfY3zQzv3YWFkwdnB/XB3t6dm+Jd3aNCdwU27O9Wt50tqvHq6O9jjaWvNF1w5UqeTEpTznsvTnGYyauZCp3/tjZKj/dvkfOUf3BrXo4VsLV2sLArq3wsbUiKCTmjtEduYmjO3ems71ahR4PJjol8fSyED1On39HnrlytHWq+A7PP8piaRkXkU0d+5cBgwYwMCBA/Hw8GD+/Pk4ODiwePFijfHz58/np59+om7duri7u/PLL7/g7u7Ojh1FO75LZMxqixYtqFWrFps3b9b4vqGhIStXriQ8PJzffvuNZcuWMW/ePLWYyMhI1q9fz44dO9i7dy+hoaEMHTpU9f6yZcsYN24cP//8MxEREfzyyy+MHz9eNSzh3DnlSergwYPExMSocnnTcgsWLGD79u2sX7+eGzdu8M8//6g6SAXR09MjOzsbhUJBx44defz4seqqoU6dOrRs2ZKEhAQA1q9fz8SJE/n555+5cOECNjY2ap1lTUaOHMmpU6fYvn07Bw4c4MSJE1y6dClf3KxZs6hevToXL15k/PjxXLlyhbZt29KtWzfCwsJYt24dJ0+eVHUEAb788ktOnTpFUFAQYWFh9OzZk3bt2nHr1q3X5lQUz549Y/bs2fz9998cP36cqKgoRo3KrRIsXryYoUOH8s0333DlyhW2b9+Om5sbAOfPK3+RrVixgpiYGNXPef3222/MmTOH2bNnExYWRtu2bfn444/z7ce4ceMYNWoUoaGhVK5cmT59+qjuALythzGPiUtIwK+ut6pNR0eHul41CLkaXuByoVcj1JYBaFTPh9AClpHJZOw6eJRnGZl4eebejpPL5fw07VcG9OnxxmEHmmTl5BB+Pxo/Tze1dt9qboRGar46LqxF2w9jaliB7o193mr5rOwcrkXexa9OTbV2v9o1CYm4qXGZ0Ihb+NVWj2/kXYtrt+6Q/cr/9R9rN2FmbEiPtvmHuZSkrBwZ4Q8f41fVWa3dt6ozofcevfV661SyI/zBE8LuKy/8HsQncSL8Dk2ruRYn3XeWb1aOLN/wBL1y2ly68/brVK63gOPX043Q28U8fnccwdRQ/62P37IoKzuHa7fu4OddS63dz7smIeE3NC4TGnELP+883zkfL67dVP/OvaRQKDgdcoW7D6LxqV5N7b0pv/9Fs3q18c3znS90/jkywh8UcPzeLd6x9qpNZ8Lo4O1BBV2dEltnWZOVlcXFixdp06aNWnubNm0IDg4u1DrkcjmpqamYmRXtYrDEZgOoWrUqYWFhGt/73//+p/q3s7MzP/zwA+vWreOnn35StWdkZLBq1Srs7ZVjpBYuXEjHjh2ZM2cO1tbWTJ06lTlz5tCtm3JcnouLC+Hh4SxdupR+/fphaWkJgLm5OdbWubd53rRcVFQU7u7uNGrUCIlEgpNTwbchcnJy+Oeff7hy5QqDBw/myJEjXLlyhdjYWNWwh9mzZ7N161Y2btzIN998w/z58/nqq68YOHAgANOmTePgwYP5qqsvpaamsmrVKv79919atmwJKDtutra2+WJbtGih1gn84osv+PTTT1UVWHd3dxYsWEDTpk1ZvHgxjx49Yu3atTx8+FC1vlGjRrF3715WrFjBL7/8olrXy/+Hl16O2y2M7OxslixZgqur8pfosGHDmDJliur9adOm8cMPPzB8+HBVW926yrGBL/8fTUxM1P4f85o9ezajR4+md+/eAMycOZMjR44wf/58/vjjD1XcqFGj6NhROTZt8uTJeHp6EhkZSdWqb391HPdUeSFibqZeOTQ3NSX6cWyBy8UnJGJuZqK+jJkJcQmJam03bt+lz+DvyczKokL58vz+8wTcXrk9tmzNerS0tPi8R5e3yj8p9RkyuRxzIwP1XIwNiL+a9lbrBLh06z6bT15k88Rhbw4uQGJKijI3E2P13EyNiU/UfEsvLjGJRqZ54k2MyZHJSExJxcrMlEvXbrBp31G2/j5d4zpKUlL6c2RyBeZ5qkTmhvrEp6QXsNSbdajjQULac/ou+BcUkCOX09vPi69b1X8v821U1YWVRy/g7eqAo7kJZ27d5/DVSGTy4o3PT0or4Pg10ic+uQSO3wlD3xz8/0iB3zkTY+ITkzQuE5eYRCMN8TkyGYnJqViZK8+NqenPaPqpP1nZOUilUiZ+O0Ctk7vr6CnCI++yceHbfy+T0p8VfPymvv3x+6qw+9Hciolj6qftS2R9JaKEZgPIzMwkMzNTrU1XV1fjUM74+HhkMhkVK1ZUa69YsSKPHxfuDs+cOXNIT0/nk08+KVKeJdZZVSgUSAooKW/cuJH58+cTGRlJWloaOTk5GBkZqcU4OjqqdZAaNmyIXC7nxo0baGlp8eDBAwYMGKC63Q3KzqOxsfoX5lVxcXFvXK5///60bt2aKlWq0K5dOzp16pTvqmH06NH873//IzMzEx0dHX788Uf8/f2ZM2cOaWlp+cZSPn/+nNu3bwMQERHBoEGD1N5v2LAhR45ovl18584dsrOzqVcv91aksbExVarkHyfj46N+9X/x4kUiIyNZs2aNqk2hUCCXy7l79y5Xr15FoVBQuXJlteUyMzPz7cOJEycwNDRU/VyUB+YqVKig6qgC2NjYEBur7MTFxsYSHR2t6oi/jZSUFKKjo/Hz81Nr9/PzyzcEo2bN3BOjjY2NKoeCOquavrgHdu9j2vzcaviSmVMByHe0KxRvvKuS7zuiyH8nxsXRni2Bi0hJS2f/0ZOM+Xk2fy+chZuLE1dv3OLvjVvZtPyPAr9vhSXJsweKQuRfkPTnmYz+awOT+3XB9C1v5anlljeP15xfQPP/hbJdQtqz5/w4+w+mfvc1psZG+ZZ9V/Lvwuv34U3O3Ypi6YHTTOjRmppONkTFJ/LL5sNYGukzuK1v8ZKl5PMN6NaCCUH76PTLciQScDA3oWv96mw5e7V4ib6Q76uk4btUWOkZmYxevoHJX5TM8VsWaTw35f9mFRyPIl+7fnk9tiyaxbOMDE6HXGHG0tXYW1ekfi1PYmLj+WXxSpb/Mg5dneJXK/Pmo1BoOC+8pU2nw3C3saSmU/6iUakpoSf5p0+fzuTJk9XaJk6cyKRJkwpcJv9nXbhzxdq1a5k0aRLbtm3DykrzWOGClFhnNSIiQjVu9FVnzpyhd+/eTJ48mbZt22JsbExQUBBz5sx57fpe7rhEIkEulwPKW/r166tXEbS0tApcR2GWq1OnDnfv3mXPnj0cPHiQTz75hFatWrFx40ZV7I8//kj//v2pUKECNjY2qtzkcjk2NjYax3y+7QNTL2cF0HQw5KWvr35Slcvl+Pv789133+WLdXR0JCwsDC0tLS5evJjvczMwUK9SuLi45NuHl7M9vJqLprHH5cqVU/tZIpGolilfvny++LdVmC/Mq7m8+v9WEE1f3IDvh7Il8JVxzi/2OT4hUe3hpqdJSfmqra+yMDMl/ql6FfVpYhIWeS4EdMqVw8neDoAaVStz9foNVm/cypQfh3Px8hWeJibRokfuE/YymZyZfyxj1YatHN6wusDtv2RiWAEtqZT4lFS19oSU9HzVqsKKinvKo/hEhi74R9Umf/F/XuPr8ez6+Xscrd78IJipkZEytzxV1KdJKZibaO5oWpqa5I9PTkFbSwsTIwMi7z/k0ZM4Bk+elS83z06fsWfZXBxt1CsFxWGiXx4tqSRfVSch7RnmhhXeer0L9pzkYx9PejRUXoBVtrXkWVY2k9btx791Q6Rv+cvrXeVrZlCB3wd2JTM7h6T051gZGzB3x3HszAsuMBQqX4MXx2+eKmpCajGO39gEHsUnMXShhuP3mwnsmja8UMdvWZT7nUtSa3+anIy5qeb/K+V3Lk98Uu537iWpVIqTnfIOmYerM3cePOLPdVupX8uTa5F3eJqUTPdhuQ/vyuRyLlyJYM32vYTt/BctrTdXD030KyiP35Q8x0Naer5q69t4npXNnksRfNuhUbHXVaJKqLIaEBDAyJEj1doKekDewsICLS2tfFXU2NjYfNXWvNatW8eAAQPYsGEDrVq1em2sJiXSWT18+DBXrlxhxIgR+d47deoUTk5OjBs3TtWm6ZZyVFQU0dHRqtvTp0+fRiqVUrlyZSpWrIidnR137tzhs880TyOi8+LKTCaTqdoKsxyAkZERvXr1olevXvTo0YN27dqRkJCgGlNhYWGhGlP5qjp16vD48WO0tbULHOfq4eHBmTNn+OKLL1RtZ86c0RgL4OrqSrly5Th37hwODsppN1JSUrh16xZNmzYtcLmX+Vy7dk1jrqB8+EwmkxEbG1vgNBOv8/IW/atTk4WGhhZpHYaGhjg7O3Po0CGNU2SBsoP56v9jXkZGRtja2nLy5EmaNMmdBiU4OFitIv02NH1xdZJj1L68CoUCSzMzgs9folpl5WedlZ3N+dAr/DBoQIHr9qruQfCFS/TvlTvF1KnzF/HKM4YrL4UCsrKUHeSP27aioU8dtfcH/jCWzm1b0rVDG02L56OjrU01J1uCr0XSqo6nqj04PJIWtQuequZ1KtlYsm2y+kXSb1sOkJ6Rydg+nbA2K1wHRaecNp5uLgSHhNH6lWmjgkOu0KKBt8ZlvDzcOXJWfUz3qUtheLpXopy2NpUcbNm+6Ff13FavJ/35c+XDW28xm8Jr90Fbi2r21gTfuE+rmrl3MYJv3KdFdc3fzcLIyMpBmudiTEsiRQEoUPC2daR3le9LuuW0qWhiSLZMxv6wm7TzKt7T1KrjNzySVnVyvzvB4ZG08Hrb49eCbZPVp8b7bcvBF8dvx0Ifv2WRTjltPN0rEXwpjNavPFwYfCmMFg01T92m/M5dVGs7dfEynpWV37mCKBQK1cV+A68abF86W+39sXMWU8nBloGfdC5URxVeHL8O1gTfuEerWrnHVvD1e7So4V6odbzO3pAIsnJy+Khu9WKv631U0C1/TXR0dPD29ubAgQN07dpV1X7gwAE6d+5c4HJr167lq6++Yu3atapheUVV5M5qZmYmjx8/RiaT8eTJE/bu3cv06dPp1KmTWofsJTc3N6KioggKCqJu3brs2rWLLVu25IvT09OjX79+zJ49m5SUFL777js++eQT1bjFSZMm8d1332FkZET79u3JzMzkwoULJCYmMnLkSKysrChfvjx79+7F3t4ePT09jI2N37jcvHnzsLGxwcvLC6lUyoYNG7C2ti5UZbRVq1Y0bNiQLl26MHPmTKpUqUJ0dDS7d++mS5cu+Pj4MHz4cPr164ePjw+NGjVizZo1XLt2jUqVKmlcp6GhIf369ePHH3/EzMwMKysrJk6ciFQqfWOZffTo0TRo0IChQ4fy9ddfo6+vT0REBAcOHGDhwoVUrlyZzz77jC+++II5c+ZQu3Zt4uPjOXz4MDVq1KBDhw6vXb+bmxsODg5MmjSJadOmcevWrTdWyDWZNGkSgwYNwsrKivbt25OamsqpU6dU86i+7Mz6+fmhq6urcQjCjz/+yMSJE3F1dcXLy4sVK1YQGhqqNgTibWj64ioyEtR+lkgkfPFJF5b+E4STgx1O9nYs/Xsterq6dGqd2wEfPe1XrCws+GHQVwB83qMLn387imVr1tGyUUMOnTzN6QshrPljrmqZuUsDadKgLtZWlqQ/e87uQ0c5FxrGstnKOW5NjY3y3crW1tbGwsyUSo6a5xTUpH8bP0b/tRFPZzu8XB3ZcPw8MQnJ9Gqq/GU1d9M+YhNTmDEwdz7BiKhoAJ5lZJKQmk5EVDTltLVxs7VCt1w53O3Vr6yNXswakLf9jbl17cjoOX9Q3b0SXlUrs37vIWLi4undQXk1PmfFWmKfJjJz1BAAendoxZod+5n+59980q4Foddvsmn/EWb/pDyedHV0qOys/tkYGigrhq+2pz/PICo6t2Lw8EkcEbfvYWxogK2VRdH2oZkPo9fswtPBGi9nWzacvkxMYgq9/JQPsczdcZzY5FRm9M09cUe8mNLpWVYWCenPiHj4hHLaWrhZK7fdzNOVVUcv4GFv9WIYQBIL9pykuacrWtLiVVneRb6X70UTm5xGVTsrniSn8cfeUygUCga0KP5sC/1b+zF6+Yvjt5IDG45fUB6/zZSdq7mb9hOblMKMAT1y841SPpj2LDPrxfEbo8z35fFrV8Dxa1dyVffC0NXXx9It9/eDhYsz9rVqkJ6QSOKDh+9km/27dWL0rIVUr1wJL4/KrN99kJjYeNVcxXMC/yU2PoGZPynHo/fu1IY12/cxfekqPmnfktCIm2zad5jZY3KfQ1gatIXq7q442lYkOzuHY+dD2HbwOBO/VT6/YVChPJWdHdXyKK+ni4mhYb72N+bfvB6j/96hPH5d7NgQHKo8fhvVBmDu9qPK4/fzj1TLqI7fzGwS0l4cv1pauNmof9c3nQ6jZc3KmOiX3F3BElHMYWBva+TIkXz++ef4+PjQsGFD/vzzT6KiolTDHQMCAnj06BGrVyvv8q1du5YvvviC3377jQYNGqiqsuXLl3/tMM68itxZ3bt3LzY2Nmhra2NqakqtWrVYsGAB/fr1U90mflXnzp0ZMWIEw4YNIzMzk44dOzJ+/Ph84yHc3Nzo1q0bHTp0ICEhgQ4dOqg9NT9w4EAqVKjArFmz+Omnn9DX16dGjRqqh4m0tbVZsGABU6ZMYcKECTRu3JijR4++cTkDAwNmzpzJrVu30NLSom7duuzevVvjvuQlkUjYvXs348aN46uvviIuLg5ra2uaNGmiKon36tWL27dvM3r0aDIyMujevTuDBw9m3759Ba537ty5DBo0iE6dOmFkZMRPP/3EgwcP0NMreMogUI7PPHbsGOPGjaNx48YoFApcXV3p1auXKmbFihWqB5wePXqEubk5DRs2fGNHFZQVz7Vr1zJ48GBq1apF3bp1mTZtGj17Fm2C5H79+pGRkcG8efMYNWoUFhYW9OiR+0tlzpw5jBw5kmXLlmFnZ6eaFutV3333HSkpKfzwww/ExsZSrVo1tm/fjrt78a+kC2Pgp5+QkZnFlDm/k5yWSk2PqiyfOx2DCrm3TaOfxCF55VZNnRqezJk4lt/+WsmCv1bjYGfD3MljqfXKnJ9PE5P4ados4p4mYKhfgSquLiybPS3fLALF1b5eTZLSnrF4xxHiklNxt6vI0uFfYGehvDCIT0olJs8chd0n5z64du1+NLvOXsbW3ISDv/5Yorl1aNqQpNRU/vh3M3EJSbg7O7B08mjsKior+3GJSUTH5c7/aG9txdIpPzHjz7/5d+d+rMxNGeffj7aNivbg0dVbd+g3Zqrq5xnL/gagS6smzBg5uEjral+nKknPnrN4XzBxKem421iw1L87di8qdPEpacQkqg/D6D47dwjHtQdP2HUxAltTIw5OVP4BkkFtGiKRwG+7TxKbnIapfnmaV3dleIei3yX5L/LNypHx2+6TPHyaRAVdHZp4uDCzb0dVJ7BY+darQVL6K8evbUWWDv8cuxcP9sQnpxKTZ87V7lPyHr9hyuN35n83n2lhOPnUZuTR3aqfe85TPnx0euUaVn1ZtOOwsDo081V+59ZsIi4hEXcnB5ZOC8j9ziUk5v/OTQtgxtJV/LtjH1Zmpowb/CVtGzdQxTzPyGTK73/xOP4pejo6uDjY8etP39KhWfHHV+fVvo4HSenPWbzvFHHJL47fQT3zHL/qcwZ3/3WF6t/XHjxm18VwbM2MODhpiKr9XmwCl+485K8hvXjvFPMC9W316tWLp0+fquafr169Ort371Y9nB4TE6M25+rSpUvJyclh6NChajM89evXTzXdaWFIFO/Ln04SCpSeno6dnR1z5sxhwICCbzML74Yi9l5pp1Ak8psXSjuFIpHaaL7L8L6S38w/jZxQwgzK1m33oU3K1nl58d0TpZ1CkchvlK3vnFbb4v9hkTeR7fmrRNaj1X5giaznXSuxB6yEkhMSEsL169epV68eycnJqmmfXjcmRBAEQRCED0QpDQMoLaKz+p6aPXs2N27cUA1oPnHiBBYWRRs3JwiCIAjC/0MlNBtAWSE6q++h2rVrc/HixTcHCoIgCIIg/D8nOquCIAiCIAhliRgGIAiCIAiCILy3Smk2gNLyYe2tIAiCIAiCUKaIyqogCIIgCEJZIoYBCIIgCIIgCO8tMRuAIAiCIAiC8N76wCqrH1bXXBAEQRAEQShTRGVVEARBEAShLBHDAARBEARBEIT3llQMAxAEQRAEQRCE94KorAqCIAiCIJQlYhiAIAiCIAiC8N4SswEIgiAIgiAIwvtBVFYF4Q3SvuhZ2ikUSYVenUo7hSKRR90u7RSKRKvLoNJOoUgU6cmlnULRpSWUdgZFsvjuidJOoUgGuzQu7RSK5I9//1faKbx/xDAAQRAEQRAE4X0l+cCGAYjOqiAIgiAIQlnygVVWP6y9FQRBEARBEMoUUVkVBEEQBEEoSz6wyqrorAqCIAiCIJQl4i9YCYIgCIIgCML7QVRWBUEQBEEQyhIxDEAQBEEQBEF4b31gU1d9WF1zQRAEQRAEoUwRlVVBEARBEISyRAwDEARBEARBEN5bYhiAIAiCIAiCILwfRGVVEARBEAShLBHDAATh/REcHEzjxo1p3bo1e/fuLe10Xqtcpx7o9OiLxMwC+f07ZC6Zi+xaqMZYrZp1qPDr0nzt6QN7IH94P1+7dtPWlA/4hezgo2RM+bFE8l176SaBZyOIS3uOm4UxY1p54+NgpTH2wI0HBIXc4vqTRLJkMtwsjBnaqAaNKtmqxaVkZPHb8cscuPGAlIws7E0M+LFFbZq62hU/3/MRBAZfIS71OW5WJoxpWx8fJ2vN+UbcI+jCda4/TiArR4ablQlDm9amkZu9xvjdV+8watNRWlRx5PferYqdK4BCoeD3pctYt2krKamp1KruyYSAH3F3dS1wmVu3b7Ng0Z9ci7jOo5gYAkaNoP9nfdRizl+8xPLV/3A1/Dpx8fH8MfdXWjVv9nb5Bf7N+u27SElNo2a1qkwY+S3ulZxfu9y+oydY8NdKoh7F4Ghnw/dff0nrpo00xi79ey3zlgbyRc+ujB0+BIDsnBx++3MFx86c42H0Ywz0K+DrU4eRgwdQ0cKiwO3+u2MfyzfuIC4hCTcne8YO6odPdY8C48+FhTPjz9VE3n+IlbkpA3t+TO+OrVXv7z95lqXrthIV/ZicHBlOdtZ82a0TnVs1UVvPk/gEZi9fw/ELoWRmZeFsZ8O0EYOo7l7ptZ/Tvzv2sXzD9lfy7Y9PjTfku3SVer6d2qjnG7RFPd/uH+XL96WlQVuYt2ItX3TpwNjB/V+ba3G4NfalzY/DcfT2wsTWhsVd+nB52653tr2CrD0Xrn5+aNeg4PND+D2CLkSonx+a1Sn4/HDldu75oU9rjTH/OfFHAQTh/REYGMi3337LyZMniYqKKu10CqTdpDW6/iPJClrBs6F9kV0Npfy035BYVnztcmkDupPWp53qJY9+kC9GYmWN7sDh5Fy5VGL57om4z/SDl/D39WTTl+3xdrDCf/1RopPTNcZfeBCLr7M1Sz5pxob+7ajnVJEhG48T/jhBFZMlkzEw6DCPktOZ37Uxu775iMnt6lHRoELx8716h+l7z+LfuBab/Dvj7VgR/zX7iU5O05zv/cf4VrJlyaet2fDNx9RztmHI2oOExzzNF/soKY1Z+8/h7fj6/6uiWrZyNSv+WcuEMT+y8Z+VWJib8+Wgb0lL1/wZAzzPyMTe3o4fvhuKpYW5xphnzzOoUtmdCWOKd9Hy15p1rFy3ifEjh7Hhr9+xNDfjqxGjSXv2rMBlQq6GM3LiND5u24ptK5fwcdtWjJgwjcvXIvLFXom4wfrtu6niqt6py8jIJPxmJEP69WVT4CIW/jyRew8eMmT0hAK3u/tYMNOXrmJQ765s+WMGPtWr8s3/phMdG68x/uHjWPzHK+O2/DED/15d+HnxCvadPKuKMTY0YFDvrgTNm8q2xb/SrU0zxs5dzIkLoaqY5NQ0+oycgLa2FsumBbBz6RxGf/05RvqvP6Z3Hw1m+pKVDOrTjS2LZuJT3YNv/vfL6/P933R8qnuwZdFM/Ht3VeZ74ox6vn26ETR/GtuWzKJbm+aMnbNILd+XrtyIZP3ug1RxcXptniVBV1+fh5evEjRs1DvfVkFyzw9ebBrUBW9Ha/z/2Ud00uvOD3Ys+awNG/w7U8/ZliH/HiA8Jv//z6Ok1Hdyfig2ibRkXmVE2clU+OCkp6ezfv16Bg8eTKdOnVi5cqXa+9u3b8fd3Z3y5cvTvHlzVq1ahUQiISkpSRUTHBxMkyZNKF++PA4ODnz33Xekv6az8LZ0un1K9r5tZO/dhvzBPTKXzkUe94RynXq8djlFUgKKxKeqF3K5eoBUit7oqWT98yeKx9Ellu/Kc9fpXqsSPWq54WphTEArb2yMKhAUcktjfEArbwY0qEYNG3OczYwY0dQLJzNDjkY+UsVsDrtDckYWC7s1oY69JXbG+ng7WFG1omnx8z1zle61K9OjThVcLU0IaNcAG2N9gs5f15xvuwYM8KtJDTtLnM2NGdHSBydzI47eVL/gkcnljN58lGHN6uBgaljsPF9SKBSs/jeIQQP606Zlcyq7uTJz6kQyMjLYuWdfgcvV9KzG6BHf0bFdG3TK6WiMadrIlxFDB9OmZfPi5bdhC4O+6EObpo2pXMmFGeN+JCMzk537Dxe43Or1m/H18cb/8z5UcnLE//M+NPCuzar1m9Xi0p89Z9Tk6Uz9aQRGhgZq7xka6BM4fybtWzalkqMDXtWr8b8Rw7h24xbRj2M1bnfl5l10b9uCnu1b4uqorFJaW5qzdud+jfFBuw5gY2XO2EH9cXW0p2f7lnRr05zAjTtUMfVredLarx6ujvY42lrzRZcOVHFx5NK1G6qYvzZsx8bSnOk/DKFmFTfsra1oWLsGjraaK3a5+e5Uz3dwf6wtLQrOd+d+bKwsGDs4T76bXpNv1w5UqeTEpWvq34H05xmMmrmQqd/7Y2So/9o8S8K1vQfYPn4qoVt2vDn4HVl5+ird61Smh/eL80P7F+eHC/kvogAC2jdgQKNXzg+tXpwfbqgXC2RyOaM3HWNY8zo4mBr9F7siFEB0VoX31rp166hSpQpVqlShb9++rFixAoVCAcC9e/fo0aMHXbp0ITQ0FH9/f8aNG6e2/JUrV2jbti3dunUjLCyMdevWcfLkSYYNG1ayiWprI3WviuzSWbVm2aWzaHnUfO2i+n/8g/6/eyg/fRFaNb3zva/z6UAUSYlk79teYulmyWSEP07Az9lGrd3X2ZrQR5orP3nJFQrSs7IxLp/boTpy6yG17CyYtv88jRds5uO/drE0+BqyvB3wt8k3+il+rupDDnwr2RH6UHPnRmO+mdkYl9dVa190LBRTfT2616lcrBzzevgomrj4pzRq2EDVpqOjQ13vOoRcDivRbb2Nh9GPiXuagF89H1Wbjo4Odb1qEnI1vMDlQq+G41dP/ThtVN+H0DzLTJm7kGa+9fGtW6dQ+aSmpSORSDR2rrKyc7h26w5+ddS/S351ahEScVNznhE38atTSz1P71pcu3WH7JycfPEKhYLTIVe4+zBG7Vb94TMXqF65EsOnzcW319d0HTqa9XsOvXZfVPl6q2/fz7smIeE3NC4TGnELP2/1/Wvk48W1m2/I90E0PtWrqb035fe/aFavNr51Xn/u+f8iK0dGeHQ8fnmGGvm62hH6oJDnB/mbzg9VSizfEiORlMyrjBBjVoX31vLly+nbty8A7dq1Iy0tjUOHDtGqVSuWLFlClSpVmDVrFgBVqlTh6tWr/Pzzz6rlZ82axaeffsr3338PgLu7OwsWLKBp06YsXrwYPT29EslTYmSCREsbeWKCWrsi8SlSM823cuUJT8mY/zOyyAgop0O5Fh0oP2MRz38ahOxqCABa1WpSru3HPBv6WYnk+VLSs0xkCgXm+ur7b65fnvj0mEKtY8W5CJ5n5dCuau5txodJ6Zy9/4ROns4s+aQZ9xNSmLr/AjK5nCGNahQ/X4Py6vkalCf+dsG3rNXyDb7K8+wc2nm6qNouRT1hc8hNNg/q8ta5FSQuXjncwNzMTK3dwtyM6JjCfcbvUlyC8lg1NzNRazc3NSX6yZMCl4tPSMTcVL1Sbm5qSlxCournXQePEH7zFhuX/VGoXDIzs5iz5C86tW6BgX7+zmpiSgoyuRxzU+M82zUmPiFJ4zrjEpNppCE+RyYjMTkVK3PlPqSmP6PpZ4PIys5BKpUycdgAtU7xg5hY1u48QP9uHfHv3ZWwG5H8vHgFOuW06dKqqcZtq/I1ybN9E2PiEwvKN4lGGuI15vupf26+3w5Q6+TuOnqK8Mi7bFw4XeN2/j9Kepbx4nyW5/ygX574tOeFWseK01c0nx8u3WDzoK4lmm+JKUO38EuC6KwK76UbN25w7tw5Nm9W3l7U1tamV69eBAYG0qpVK27cuEHdunXVlqlXr57azxcvXiQyMpI1a9ao2hQKBXK5nLt37+Lhkf9hh8zMTDIzM9XasuRydKWFOTEo1H+USFSV4HyRD++T/cqDVJkRV5BaVkSnR1+eXw2B8hXQ+2kKGb/9giIluRDbLrq8F9UKFEh485X2rvB7LDp5hYXdm6p1eOUKBWb6ekxuVw8tqRRPazNi054TeDaiWJ1VVb55clMoCpnvldssOhbCwt4tVb/Q0jOzGb3lGJM/8sO0QvEvWrbv3svEabkdhKUL5ilzluTPuTSqGTv2H2LirPmqn5f8Og3I/5lSiGMgf/oKVVvMk1h++W0Ry+fOQFdX8zCGV2Xn5DBy0s8oFAom/vDt67ebNy+FIt/nqx6fN03Fi/xz39Evr8eWRb/y7HkGp0OvMOPP1dhbW1G/lueLReR4ursy8kvlQ27V3FyIvP+QtTsPFNhZVW0//xfstZ9t/n0pKN9ZPMvI4HTIFWYsXY29dUXq1/IkJjaeXxavZPkv49DVefNn//+Nho+7EGeHF+eHoyEs7N1KdUGcnpnF6M1HmfxxI0z1S6aoIRSP6KwK76Xly5eTk5ODnV3urR2FQkG5cuVITExUdlQ0dQReIZfL8ff357vvvsu3fkdHR43bnT59OpMnT1ZrG+Nqw1i3gp9mV6QkoZDlIDU159Ub3hITMxR5qq2vI7t+Be0W7QGQ2tgjtbaj/OQ5r6xQ2WE22HWa9IE9UMQ80rSaNzKpoIuWREJ8WoZae0J6Rr5qa157Iu4zfvdZ5nVphK+z+rg9S4PyaEslaL3Ssa9kbkx8egZZMhk6WlrFzFe9ipqQnpGv2pov36t3GL/9JPN6tsC3Uu7/YVRiCo+S0hi69qCqTf7i+KkxZQW7hnXH0azwY9RaNG1Mreqeqp+zsrMAiH/6FCvL3CfcnyYkYpGn2vpfaN6oITWrVc3NLytbmV9CIlavPMj1NDEJc7OCxxhbmJkS/0oV9eUyFi+qrddu3OJpYhLdBw5RvS+Tyblw+QprNm8j7PButF4cB9k5OYwYP42H0Y9ZuWCWxqoqgKmREVpSab6q5NOklHzV1pcsTY2JT0zOF6+tpYWJUe4YWqlUitOL8acers7ciXrEn+u2qjqrlmamuDmqf/ddHe3Yf0p9yE+h8k1Ofk2+Jhr3T2O+dq/k+yA332uRd3ialEz3YWNU8TK5nAtXIlizfS9hO/9FS+v/XzXOpILei/ODehU1If154c4P204w75MW+L4yjCAqIVV5fvj3gKpNdX6YHMiub3sU6fzwTpShW/glQXRWhfdOTk4Oq1evZs6cObRp00btve7du7NmzRqqVq3K7t271d67cOGC2s916tTh2rVruLm5FXrbAQEBjBw5Uq0tq8cbHmTJyUF+6zpateuTE3xU1axVux45Z44XettS1yooEpRjRuUP7pHu31vtfZ1+g5CU1ydzyRwUcQXfqn0THS0tqlmbEXzvMa2qOKjag+89poW75qlbQFlR/d/us8z62JemGjrvte0t2HXtPnKFAumLE+n9hBQsDcq/dUdVla+tOcF3omnl4Zyb751oWlTRfNEByorJ/7afZFb3ZjSt7KD2XiULY7YNVr+999vhi6RnZTO2XQOsjYv2YIqBvr5aZ0uhUGBpYc6pM2epVlU53i0rO5vzFy8xangJj5kuTH4VKmBQIfcJdoVCgaW5GcHnL1KtsltufqFh/DBoYIHr8apejeDzF+nfq7uq7dS5i3i9GDfZwKc221f/qbbM2F9mU8nJgYGf9crXUb3/8BGrFszC1LjgX/w65bTxdK9EcEgYrf1y754Eh4TRooGPxmW8PCpz5OxFtbZTl8LwdK9EOe2Cf+0pFMoxpy/VrlaFuw/Vh23cexSDrZXlm/O9lCffS2G0aFhX4zJeHu758714Gc/Kb8pXQVa28sKjgVcNti+drfb+2DmLqeRgy8BPOv+/7KgC6GhrUc3WguDbj9TPD7ejaVH1DeeHbSdenB/U4954fjB69w+uvZEYBiAIpWvnzp0kJiYyYMAAjI3VKxE9evRg+fLlbN68mblz5zJ69GgGDBhAaGioaraAlxXX0aNH06BBA4YOHcrXX3+Nvr4+ERERHDhwgIULF2rctq6uLrq66oPsUwsxBCBr87/o/TgZ2a1w5BFXKNe+K1Ira7J3bQJA58uhSM0tyZg9CYByXfqgeBKN7P4dJOXKod2iPeUat+T51J+UK8zOQn7/tvpG0tNQQP72t9C/XlVG7ziNp7UZXnYWbAiNJCblGb1quwMw92gosanPmPGRL6DsqAbsPE1AK29q2VoQ96KKoaethaGe8pZj79rurLl4k18OXKSvT2XuJ6Ty5+lwPvMp/sNL/RtUZ/SW43jaWuBlb8WGizeISU6jl4+yWjj34AViU9OZ0VV5a3bXldsEbD1OQLsG1LK3JO5FVVZPWxtDPR10tbVxt1KvIBq92I+87W9DIpHwxae9Wbp8Jc6ODjg5OrJ0+Qr09PTo1L6tKu6n/02kopUVP3w3FFB2GG/fuav695PYOCJu3KRC+fI4OSo73OnPnhH14KFqHQ8fRRNx4ybGRkbY2rz+KXW1/Hp2Zenfa3Gyt8PJwY6lq9eip6tLpzYtVHGjp87EytKCHwYNAODznl35fNhIlv0TRMvGvhw6EczpC5dYs0g57MGgQgUqV3JR21Z5PT1MjIxU7Tk5Mob/bwrhNyNZMnMqMrmcuKfKOxDGRobolCuXL9/+3ToyetbvVHd3xcvDnfV7DhETG6+aN3VO4L/EPk1g5o/KC4HeHVuzZvs+pi9dzSftWxAacYtN+w4ze8xw1TqXBm2hemVXHG0qkp2Tw7FzIWw7dJyJwwbkbrdrB/qMnMCSoC20b9KQsBuRrN99iCnDv37t59u/WydGz1pI9cqV8PKozPrdB/PnG5/AzJ9e5NupzYt8V/FJ+5aERtzUnK+7K462FcnOzuHY+RC2HTzOxG8Hvvjsy1PZWb3TVV5PFxNDw3ztJUlXXx9Lt9zpySxcnLGvVYP0hEQSXzlO36X+DaszevMxPG0t8XKwYsPF63nOD+eJTXnGjG6vnB+2HHtxfrAiLvXF+aHci/NDOW3cK6rfATHSU/5eyNsu/DdEZ1V47yxfvpxWrVrl66iCsrL6yy+/kJiYyMaNG/nhhx/47bffaNiwIePGjWPw4MGqzmbNmjU5duwY48aNo3HjxigUClxdXenVq1eJ55xz/ACZRsbofjYQiakF8vu3eT7+exSxjwGQmlkgscrtSEi0tdH5ejgSc0vIykR2/w7Pxg9Hdj64xHPTpL2HE0nPM1l86ipx6c9xtzBmac9m2L2oKManPScmJfe2+/qQSHLkCqbuv8DU/bkV7C7VXfilU0MAbIz0+atXc2YcukSX5bupaFiBvj5VGNig4InQC51v9UrKfI+FEpf2DHcrU5Z+1gY7E4MX+T4j5pU5YtdfvKHMd/dppu4+nZtvLTd+6aJ5EvWS9nX/L8jMzGTy9F9JTlH+UYDAxQvVKrAxj58gfeViKDYuji69+6p+Dlz9D4Gr/6Gedx3+/msJAFfDI/ji68GqmOlz5gPQ9aOOzJgysdD5DfysFxmZWUyZu5Dk1FRqVqvK8nkz1Cqw0U9ikbwy+XidGp7MmTSO35atZMFfq3Cws2HulHHU8iz8//HjuDgOn1T+n3T5cpDae6sWzKZ+nqf4ATo09SUpJZU/1mwiLjERdycHlk4dg11FZYUzLiGJ6NjcOXTtra1YOnUMM5au4t+d+7AyM2Xc4C9p26i+KuZ5RiZTfl/O4/in6Ono4OJgx68/DaNDU19VTI0qbiyc8ANzV6xl0ZpN2FtbEjCoHx+1aPzafezQzJek1Bf5JrzId1rAK/kmEh2XO/OGvbUVS6cFKPPd8Uq+jXNnk1Dm+1eefL+lQzPffNv/Lzn51Gbk0dy7XD3nKcdun165hlVfDi5osRLVvnolkp5lsPhYSJ7zg3I6uvjU58S8Mifz+gvXCzg/uPNL1//m/FBshXqO4v8PiaKgJ0AEoYz5+eefWbJkCQ8e5J9YvzhS22m+dfe+qtCrU2mnUDS6ZesBBq0ug94c9B5RpL+bB/TeqbTCj/V+L5Sx8YODXV7f2X7f/PHv/0o7hSLR6vPTO9+G4saZNwcVgqRKgzcHvQdEZVUosxYtWkTdunUxNzfn1KlTzJo1q+TnUBUEQRAEoVSJzqpQZt26dYtp06aRkJCAo6MjP/zwAwEBAaWdliAIgiC8W+IBK0EoG+bNm8e8efNKOw1BEARB+G+VsaEnxSU6q4IgCIIgCGXJB1ZZ/bD2VhAEQRAEQShTRGVVEARBEAShLBHDAARBEARBEIT31gc2z+qHtbeCIAiCIAhCmSIqq4IgCIIgCGWJGAYgCIIgCIIgvLfEbACCIAiCIAiC8H4QlVVBEARBEISyRAwDEARBEARBEN5fH1ZnVQwDEARBEARBEN5borIqCIIgCIJQlnxgwwBEZVUQBEEQBKEskUhK5vUWFi1ahIuLC3p6enh7e3PixInXxh87dgxvb2/09PSoVKkSS5YsKfruKhQKxVtlKwgfCNmGuaWdQpHI9u4t7RSKRPuHiaWdQtHIZaWdQZEokuNLO4Wiu3y2tDMoGteqpZ1B0STElXYGRTL002mlnUKRLFGkvPNtKB5eL5H1SOyLduyuW7eOzz//nEWLFuHn58fSpUv566+/CA8Px9HRMV/83bt3qV69Ol9//TX+/v6cOnWKIUOGsHbtWrp3717o7YrKqiAIgiAIgvBGc+fOZcCAAQwcOBAPDw/mz5+Pg4MDixcv1hi/ZMkSHB0dmT9/Ph4eHgwcOJCvvvqK2bNnF2m7orMqCIIgCIJQlpTQMIDMzExSUlLUXpmZmRo3mZWVxcWLF2nTpo1ae5s2bQgODta4zOnTp/PFt23blgsXLpCdnV3o3RWdVUEQBEEQhLJEUjKv6dOnY2xsrPaaPn26xk3Gx8cjk8moWLGiWnvFihV5/PixxmUeP36sMT4nJ4f4+MIPURKzAQiCIAiCIHyAAgICGDlypFqbrq7ua5eR5HkwS6FQ5Gt7U7ym9tcRnVVBEARBEIQypWSmrtLV1X1j5/QlCwsLtLS08lVRY2Nj81VPX7K2ttYYr62tjbm5eaHzFMMABEEQBEEQypJSmLpKR0cHb29vDhw4oNZ+4MABfH19NS7TsGHDfPH79+/Hx8eHcuXKFXrborMqCIIgCIIgvNHIkSP566+/CAwMJCIighEjRhAVFcWgQYMA5bCCL774QhU/aNAg7t+/z8iRI4mIiCAwMJDly5czatSoIm1XDAMQBEEQBEEoS0rpL1j16tWLp0+fMmXKFGJiYqhevTq7d+/GyckJgJiYGKKiolTxLi4u7N69mxEjRvDHH39ga2vLggULijTHKojOqiAIgiAIQhlTen9udciQIQwZMkTjeytXrszX1rRpUy5dulSsbYphAIIgCIIgCMJ7S1RWBUEQBEEQypJSGgZQWkRnVRAEQRAEoUwRnVVBEARBEAThfSUqq8KH6sGDB0yaNIk9e/YQHx+PjY0NXbp0YcKECYWevPfevXu4uLgQEhKCl5fXu034PbP27DUCT1wmLu0ZblamjOngi4+zjcbYA9fuEHQunOsxT8mSyXCzMmVoCx8auTuoYjacj2Bb6E0inyQAUM3Wku/b1KOmvVWJ5Ctt/hFabXuCiRmKR/eRBS1GcevqG5eTuFVD+6c5KB7dI2fyYFW79o+zkFatlS9eHnaWnN/GFym3f/ccJnDrXuISk3BzsCNgQB98qlUuMP7c1RvMXBFE5INHWJmZMKBLe3q3a64Wk5L+jPn/bOLA2UukpKVjb2XJT1/2oql3TQB+D9rKH+u2qy1jYWLEiRXz35zv3iMEbttHXGIybg62BHzZ6/X5XrvBzJXriXwQjZWpCQO6tKV322aq97+YMIvz127mW65JnRosHfedMt912/lj/Y78+S6f88Z8NVl7+DSBe08Ql5SKm50VY/p0wqeyi8bYuKQUfl23m2v3HnE/9il9WzYk4NOP1GIOXLzKnzuPEhX7lByZDMeKFnzZthEf+9Z5q/zy5Xv5DoGXIolLz8DN3JAxTWrgY2ehMfZAZDRBYXe5Hp9MlkyOm5khQxtUpZFT7kTm2TI5yy7cZFtEFE/SMnAxNWCknyeNnTVPdl7kfE9cIvDQWeJS0nCztmBM91b4uDpojI1LTuPXrYe59uAx9+MS6NvEh4DurdRi+i1Yw/nIB/mWbVLNlSWDehY/33PhBAZfIS71OW5WJoxp1wAfJ2uNsQfC7xF0IYLrjxPIypHhZmXC0GZ1aORmrzF+95XbjNp0lBZVHPm9T+ti51oUbo19afPjcBy9vTCxtWFxlz5c3rbrP81BKDrRWRUAuHPnDg0bNqRy5cqsXbsWFxcXrl27xo8//siePXs4c+YMZmZmpZ3me2vPlUim7w5mwkeNqO1ozfrz4fiv3s2O7z7B1sQwX/yFezH4utnzfet6GOrpsuXSdYb8s5cg/65Us1X+wj13N5qONd3wcqyIrrYWy09c5uuVu9j+3SdUNNIvVr7Suk3R6j0I2T8LkUdeQ6tpR7S//5ns8QMhIa7gBctXQHvATygiQsDIVO2tnEVTQCv3lCIxMEJ70hLkF44XKbfdJ88xI3At47/5nDpV3Vi3/yj+U+exY8E0bC3zXzQ9fBLHoGnz6NG6Cb9+/zWXrkcy9c+/MTM2pE1DHwCysnMYMGk2ZsZG/PbjECqam/I4PgH98npq63JzsCNwcu78f1rSN1cvdp86z4wV6xj/9Wcv8j2G/88L2DF/csH5/ryAHq0a8+vwgcp8l63BzMiQNg29AVjw4xCyc3JUyySlptH1hym0e/F+br62BE7M/VOJWtK3e2Z2z7kwpq/dxYTPO1PbzYn1R8/iP28lO6aNwNbcJF98Vo4MU0N9/Ds1Z9WBkxrXaaxfAf9OzXGxsaScthbHLl9nXOAmzIwMaFS94I58ofK9+ZDpx68woXktatuas/7KXfy3nWZH35bYGlXIF3/hUTy+jlZ871sNQ91ybAmPYsj2MwT1ako1K+X+LTgdwY7rD5jc0otKZoacuh/LdzvPsuaTJqqYt873UgTTNx9kQs+21K5kx/pTofgvXs+OsQOxNTPOF5+Vk4OpQXn82zRk1ZHzGtf524BuZMtkqp+T0p/TbWYgbWtXKVauAHuu3mH63rNM6OhLbceKrL9wHf9/9rFjaHdsTQzyxV+4/xjfSnZ839IHQz0dtoTcYsi/Bwj6+iOq2ahfQDxKSmXW/nN4O5bMRUBR6err8/DyVYJX/MOgzWtKJYcS8YFVVsVsAAIAQ4cORUdHh/3799O0aVMcHR1p3749Bw8e5NGjR4wbNw5Q/i3frVu3qi1rYmKimq7CxUVZialduzYSiYRmzZqp4gIDA/H09ERXVxcbGxuGDRumei8qKorOnTtjYGCAkZERn3zyCU+ePFG9P2nSJLy8vAgMDMTR0REDAwMGDx6MTCbj119/xdraGisrK37++We13JKTk/nmm2+wsrLCyMiIFi1acPny5RL85JRWnrpCd++q9PDxwNXKlICOftgYGxB0LlxjfEBHPwY09qKGvRXOFsaMaFMfJ3Njjl6/r4qZ9UlL+tT3xMPGgkqWpkzp0gS5QsGZ24+Kna+0TXfkJ/YiP7EXYh4gC1oCCXFoNfvotctpffE98rNHUNyOyP9meiqkJKpekmp1ICsD+fkTRcpt1fZ9dGvZmJ6tm+DqYMvYAZ9ibW5G0N4jGuOD9h3FxsKcsQM+xdXBlp6tm9CtRWMCt+5TxWw+dILk1HR+HzOMOh7u2FlZ4F2tMlVdHNXWpa0lxdLUWPUyMzZ6c747DtCtRSN6tmqMq70NY7/qjbW5KUH7jmnOd/8xbCzMGPtVb1zt2HQkiAAATlhJREFUbejZqjHdWvgRuH2/KsbEUF8tj+CwCPR0dWjr6/OGfPNfGBXGyn0n6N7Yhx5N6uJqa0XApx9hY2ZM0JEzGuPtLEwZ++lHdParg2GeDv9L9apWopW3J662VjhamfN5az8q21tz6ea9t8pRLd9Lt+nu6USP6s64mhkS0LQmNgblCbpyV2N8QNOaDPBxp4a1Kc6mBozwq4aTiQFH7+b+Gcjt1x/wTd3KNHWxxsFYn941XfBzsmLlpcji53vkHN0b1KKHby1crS0I6N4KG1Mjgk6GaIy3MzdhbPfWdK5XA8Pymv8Upol+eSyNDFSv09fvoVeuHG29qhY/39NX6V6nMj28q+BqaUJA+wbYGOsTdEHD9x4IaN+AAY1qUsPOEmdzY0a08sHJ3IijN9QrvzK5nNGbjjGseR0cTN/83XoXru09wPbxUwndsuPNwe81SQm9ygbRWRVISEhg3759DBkyhPLly6u9Z21tzWeffca6detQKBRvXNe5c+cAOHjwIDExMWzevBmAxYsXM3ToUL755huuXLnC9u3bcXNzA0ChUNClSxcSEhI4duwYBw4c4Pbt2/Tq1Utt3bdv32bPnj3s3buXtWvXEhgYSMeOHXn48CHHjh1j5syZ/O9//+PMmTOq9Xbs2JHHjx+ze/duLl68SJ06dWjZsiUJCQnF/txeysqRER4dh1+eW16+bvaERj0pYCl1crmC9MxsjCsU/DeaM7JzyJHJMS7gl1ehaWkjcXJHfk193jt5+EUkbtUKXEzq1waJpQ2y7X8XajPSxu2QnzsGWRmFTi0rO4drt+/j5+Wp1u7n5UnIdc2dhtAbt/PH1/bk2u17qurk4fOheFVxZeqf/9Co//d89N14lm7ciUwmV1vufswTmnw1glb+PzFyzhIePI4tZL7qn5tfLU9CbtwuIN87+NXKv3/Xbt9Xq6a+atOhk3Twq0sFPfX/+/sxsTQZOIpWg8cwcu6fPHj8mqp4QfuQk0P4/Wj8PN3V2n093QmNjCpgqaJRKBScDo/k3uM4fKpoHlpQWFkyOeGxSfg5qg+H8XWyIjSmcN9ruUJBelYOxno6r6xXhq6W+q9EPW0tLkU/LV6+OTLCHzzGr6qzer5VnQm9W/wLz5c2nQmjg7cHFXR13hz8GsrzWTx+rnZq7b6udoQ+eP334SXV+SzPuWrRsVBM9fXoXqf41V/hwyKGAQjcunULhUKBh4eHxvc9PDxITEwkLu7NvwgtLS0BMDc3x9o6d3zTtGnT+OGHHxg+fLiqrW7duoCyYxsWFsbdu3dxcFCO4fr777/x9PTk/Pnzqji5XE5gYCCGhoZUq1aN5s2bc+PGDXbv3o1UKqVKlSrMnDmTo0eP0qBBA44cOcKVK1eIjY1FV1d50pw9ezZbt25l48aNfPPNN2/xaeWX9CwDmVyBuYF6R99cvzzxac8KtY4Vpy7zPCubdtVdC4yZu/8sVkb6NMzzS6TIDI2QaGkpK6CvUCQnIq1uqnkZK1u0ug8ge+ZIkMs1x7xC4lIFqb0L2SvnFim1pNRUZHI5Fibqt0bNTYyIT0rWuEx8YjLmtdWrNBYmxuTIZCSmpGFlZsLDJ3GcvRJBpyYNWDr+e+5FP2Hqn/+QI5MztNfHANR0r8SM4QNxtrUmPimZJRt28mnAL2z/bRqmRvlvfSrzTVPmm6cCa25iWHC+ScmY5xkaYmFspMw3NQ0rUxO198Ju3eVW1COmDemn1l7T3YUZ336Fs21F4pNSWLJpF5+Om8H2+ZMxNdScr+Z9eIZMLsfcWH0ZcyMD4pNTC70eTVKfZdDsh+lk5+QglUgZ/3lnfPN0iosq6XkmMoUC8zwXdubldYlPzyzUOlZciuR5Tg7t3HO/S40cK7Iy5DbedhY4muhzJiqOw3ceIyvERfpr801/pjw/GKoP3TE31Cc+Nb1Y634p7H40t2LimPpp+2KvK+lZhvLz1dd0PnteqHWsOH2F59k5tPPMvTC5FPWEzZdusHlQ12LnKCjvcn5IRGdVeKOXFdW3/XLExsYSHR1Ny5YtNb4fERGBg4ODqqMKUK1aNUxMTIiIiFB1Vp2dnTE0zP0lX7FiRbS0tJC+Mk6vYsWKxMYqr/4vXrxIWlpavofDnj9/zu3bmqtemZmZZGaq/8LTzs5Bt9ybvyp5Px0FICnEbZZdlyNZdPgiCz9rm6/D+9LyE6HsCrvNqgEfFSqXwsnzS1giydekbJei/U0Asm2r4UnhKkHSRu2QP7yL4u6N4qeJ8hh83fGX9728x6xcrsDc2Igpg/ujpSXF09WZuIQklm/bq+qsNnnxoBVAZSd7vKq40XbwaLYdOUX/zm1fn2C+7b/+/z5fvi/bNSyz6dBJ3B3tqOmuXpFsUqfGK/mCVxVX2g4dy7YjwfT/uM3r89WUU56fFYri/0LU19Nh86RveZaZxZnw2/watAsHSzPqVa1UrPWC5s+wMOnuuvGQRWeus/Cj+mod3oCmNZhwKIROfx9EggQHY326VnNkS3jJVJfzH6MldxN20+kw3G0sqelkW0JrzP9ZKs9nb7brym0WHQ1hYe9WqvNZemYWozcfZfLHjTDV1zxsRCgi0VkVPjRubm5IJBLCw8Pp0qVLvvevX7+OqakpFhYWSCSSfMMBsrOzX7v+vEML8iqoI5K3vVy5cmrvSyQSjW3yF5U/uVyOjY0NR48ezbduExMTjblMnz6dyZMnq7WN79GGiZ8U3FkxqaCHllSSr+qQkP68wM7nS3uuRDJ+6zHm9W6FbwFPzgaevMyfx0JY/mUnqlgXblaG10pNQSGTgZH6A3MSIxMUeaqtAOiVR+pSBYmjG1qfvRhnLJEgkUop9+cecuYGoLgemhuvo4u0XjNk21YVOTUTQ0O0pNJ8VcmE5FTMCxg/amFqTHyievzT5BS0tbQweVHNsjQ1RltbC61XbvNWsrchPjGZrOwcdDRcAFTQ08XdyZ57MQUP5TAxNCg4X5MC8jUxJj4x5bX5vvQ8M5Pdp87z7YsO9etU0NPF3dGOezGFu1Wbuw8VlPuQnKa+D6lpmBdQUS4sqVSKU0XlAzYejrbciYll2a6jxeqsmpTXRUsiIT5dfXhJwvPMfNXWvPbcfMj4gyHM61AX3zzDCMwq6PL7Rw3IzJGRlJGFlb4ec0+FY6fhga0i5atfQXl+SMnz+aal56u2vo3nWdnsuRTBtx0aFXtd8OJ8JnnL89nVO4zfdoJ5n7TA95U7QFEJqTxKSmPovwdUbfIXv0dqTA5k17c9cDQrnTGsQtkgxqwKmJub07p1axYtWsTz5+onqMePH7NmzRp69eqFRCLB0tKSmJgY1fu3bt3i2bPcW906OsrxUrJXnlI1NDTE2dmZQ4cOadx+tWrViIqK4sGD3MH44eHhJCcnFzg0oTDq1KnD48eP0dbWxs3NTe1lYaF5ipuAgACSk5PVXmO6aq4Iv6SjrUU1W0uCIx+qtQdHPsTrNU+87rocydhNR/m1ZwuaVnHSGLP8RChLjlziz34dqG5n+YY9LiRZDor7t5B6qk8hJK1WB0WkhgfCMp6RPeEbciYPVr3kx3ahiHlAzuTBKO5cV19P3SZQrhzy05r/v19Hp5w2nq5OBF9WzyP48jVqV3XTuIxXFVeCL19TazsVeg1PV2fKaSs7oXU83ImKiVVdyADci36Cpamxxo4qQFZ2NncexmCZ57a85nzVHzwJDgundhXNQzq8qlQiOEx9/06FhuPp6qTK96W9py6QlZ3NR00bFJhD/nzzP13+Ojra2lRzsiU4/Jb6PlyLxMvNsYCl3o5CoRwjWxw6WlKqWZkQHKU+LCk4Kg4vm4JnLNl14yFj91/i13beNHXRPAUTgK62FhUNypMjV7A/MpoWlTRPP1fofLW1qOZgTfCNe+r5Xr+Hl0sxh/QAe0MiyMrJ4aO6/9fenYfVnPZ/AH+filalULRIKUx2MsMgWygGDTPMWEbWB2MfPRhmiifrWLL80GQ3RmPsa/ZdJpVkUKIoFJEWJVq+vz8aZxynwjOPc39P3q/r6rqc+5wx7+k6U59zfz/351vvH/9dwMufZ5Vx/rWDnOdv3Ucju5LH5u2/cgvf7zqN+b3aok0t1feNY2Uz7B75OXaM8FJ+tatdHR87VMOOEV6o+g+nm3yYPqwDVtxZJQDA8uXL8emnn6Jz587w9/dXGV1lY2OjPGXfvn17LF++HM2bN0dhYSEmT56ssrtpaWkJQ0NDhISEwNbWFgYGBjAzM4Ofnx9GjBgBS0tLeHp6IisrC+fOncOYMWPg7u6OBg0aoF+/fggICEB+fj5GjRqFNm3awNXVtaTIb+Tu7o4WLVrAy8sL8+bNQ+3atXH//n0cOHAAXl5exf7d+vr6yv7Wlwre4rK7d8v6mLztBOraVEEjOyv8Hn4dyRlP0adZ0cGbRYf/wMPMbMz9oj2AokJ16vYTmNr1UzS0s0JqVlHBb1BOFxX+OkSz5kwUlh69iJ96d4B1xQrK1xiVLwdj/XLFpHh7hYe3Q3fovyHdvoHCW9eg69YVsLBEwal9AADdnoMB80ooWPMTIEmQ7t1W/Qsy0yHlvVBfx18tAJfOF00H+C8M7N4ZU5YEoV7NGmhUuya2HjmF5Edp6PPXHNJFm7bhQdoTzBs3DADwVee2+PXAMcxdG4wvO7ohKvYWdhw7gwUT/6X8O7/yaIdf9h/F7DVb0K9LB9xJfoCft+9H/65/fxCZv/43tHVtBOsqFnickYlVv+/D05xn8Gr3ael5u3XElKVrUK+m/V95Txfl7dSmKO8vO4ryjh1SlKVTG/x68ATmrvvt77zHz2LB+GFqf/f242fR4ePGxfagzt/wO9q6NoB1ZQs8zsjCqm378fRZLrzalp63ON6dW2Ny0FbUrWGLRjWr4/dTYUhOS0eftp8U/TdsC8HDJ5mYO6y38p+5nngfAJCT+wJpT7NxPfE+yunqwsmm6APaz/tPol4NG9hVqYS8gnycjo7FntBI/DjA653zqeVtUhOTD0WgrlVFNKpmgd+v3EZyVg761C9qlVh07ioePs3F3M5Fo772x97F1MMRmOpWHw2rWiD1r11ZAz1dVPjr/6XLKWl4+DQXdaqY4cHTZ/i/CzGQJAlDXIv/kPROedt9jMmb9qKuXVU0crDB7+ejkPwkE31aNS7Ku+ckHmZkYe6Av6dxXL9btKOf8zwPaU9zcP3ug6Lv72ujoLaHRqNDg1qoaFz6ruc75W1RD5N3nEJd6ypoZGeJ3yNiin6euRZNGlh09CIeZuZgbs+i9/j+K7cwdecpTPVojoa2lq/8PNNDBYPy0C+nB2cr1Q8Spn/9nHt9/X3TNzZGFae/d/YrO9SAbcP6yE57gidJd0v5J2WGbQD0IXJ2dkZ4eDj8/PzQp08fPH78GFWrVoWXlxd8fX2VM1YXLlyIQYMGwc3NDdbW1liyZAkiIiKUf4+enh6WLl2KmTNn4scff0Tr1q1x8uRJDBw4ELm5uVi8eDEmTZqEypUr44svvgDw9zisMWPGwM3NDTo6OvDw8MCyZcv+0X+TQqHAgQMHMG3aNAwePBipqamoWrUq3NzcYGX1v53x51nfCek5z7HyRARSs3LgbGWBwAGesDEv6rF9lJWD5PS/LwNuvXgN+YWF+M/es/jP3r/nVHo1roXZvYqG2W/54yryCgoxfssRlX/XqHZNMbrDf1/EA0DhxVOAiSl0u/WDrlnRTQHyl0wHHv91CbmiBRQW/8XNB6xsoFOrPvIWTvmvs3Vp9THSs55ixdY9SH2SAefqNlg1fTxsLIt+Sac+yUBy6t+nvm2tqmDV9AmYu24Lfj14HJYWFfH9kL7KGasAUK2yBVb7foe564LhNeFHWFmYY8Bn7hj6eRfla1IeP8GkRauQnvUU5qYV0LBWTQTPm6b895aYt2Wzory/7/srrzVWfT8WNpaV/sqbjuRHr+WdNhZz123FryEnYWlhhu8Hf6WcsfpSwv0URFy/idU/Tij235vy+AkmLQ76O6+zI4LnTFX+e9+F58cNkP40Gyv3HENqRhacbawQON4bNpWLDtw9yshCclq6yj/Ty+/v/z+v3rmH/Rcuw7pSRRz9aTIA4NnzF5i5aTcePMmAfvlycKxaBfOG9YHnxw3wT3nWskX6sxdY+UcMUnOew7lSBQT2aKG8ZP8oOxfJWX9f8dl6JQH5hRL+czIa/zkZrVz3+sgOszsVfd9f5BdiSeh13M3IhlE5PbjVsMK8zk1h+g9P1wOAZ5OPkJ79DCsPnUNqRjacq1VG4IgvYfPXjNVHmU+R/FprSK/565R/vpqUgv0R12BtYYqjfqOU67cfpiEy/i5Wj1KdnPKP89ZzRHpOLlaeuoTUpzlwtjRHYL9OsKn48ufZMyS/0jayNTym6Pt7IBT/ORCqXPdq6IzZn7v9T7P9U/aujTHx5AHl4y8XzwEAhK7fjA2DRpb0j5FgCult5hERfcAKfn+3E+2iFYSEiI7wTvS+8xUd4d0UFrz5NTIiZTwSHeHdXf5DdIJ3U/OfzzbVqNJu/CFD3/b1Fx3hnaySMt/8on/qSfKbX/M2zP9Zm4umcGeViIiISKuwDYCIiIiI5OoD61nlNAAiIiIiki3urBIRERFpkw9rY5XFKhEREZF2+bCqVbYBEBEREZFscWeViIiISJt8YAesWKwSERERaZMPrFhlGwARERERyRZ3VomIiIi0yoe1s8pilYiIiEibsA2AiIiIiEgeuLNKREREpE0+sJ1VFqtEREREWoXFKhERERHJ1Qe2s8qeVSIiIiKSL4mINC43N1fy9fWVcnNzRUd5K8z7fjHv+6dtmZn3/dK2vB86hSRJkuiCmehDk5mZCTMzM2RkZMDU1FR0nDdi3veLed8/bcvMvO+XtuX90LENgIiIiIhki8UqEREREckWi1UiIiIiki0Wq0QC6Ovrw9fXF/r6+qKjvBXmfb+Y9/3TtszM+35pW94PHQ9YEREREZFscWeViIiIiGSLxSoRERERyRaLVSIiIiKSLRarRERERCRbLFaJiIiISLZYrBJRifLz83H06FEEBgYiKysLAHD//n08ffpUcLKyJzMzE7t27cL169dFRyF6ay9evEBsbCzy8/NFR3kr6enpWL16NaZOnYq0tDQAQGRkJO7duyc4GZWGo6uINCgyMhLlypVD/fr1AQC7d+/GunXr4OLiAj8/P5QvX15wwr/duXMHHh4eSExMxPPnz3Hjxg04Ojpi/PjxyM3NxapVq0RHLNamTZuwatUqJCQkIDQ0FPb29ggICICDgwN69OghOp5S79694ebmhtGjR+PZs2do2LAhbt++DUmSEBwcjF69eomOqLX27NnzVq/r3r37e07y7goLC3Hz5k08fPgQhYWFKs+5ubkJSqUuJycHY8aMwYYNGwBA+fNh7NixsLa2xpQpUwQnVBcdHQ13d3eYmZnh9u3biI2NhaOjI3744QfcuXMHGzduFB2RSiIRkca4urpK27ZtkyRJkm7duiUZGBhIX3/9teTk5CSNGzdObLjX9OjRQ+rfv7/0/PlzycTERLp165YkSZJ08uRJycnJSXC64q1YsUKqXLmy5O/vLxkaGiozr1u3Tmrbtq3gdKqsrKykqKgoSZIkafPmzZKTk5OUnZ0trVixQmrUqJHgdMVLSUmR+vfvL1WrVk3S1dWVdHR0VL7kQqFQvPFLTnlfCg0NlRwcHCQdHR3Z5x07dqzUtGlT6cyZM5KxsbHy/7Xdu3fL9v3boUMHycfHR5IkSeVn2rlz5yR7e3uByehN9EQXy0Qfkhs3bqBRo0YAgN9//x1ubm749ddfce7cOXz11VcICAgQmu9VZ8+exblz59R2e+3t7WV7yWzZsmUICgqCl5cX5s6dq1x3dXXFpEmTBCZTl5GRAQsLCwBASEgIevXqBSMjI3Tt2hU+Pj6C0xXP29sbiYmJ+OGHH1CtWjUoFArRkYr1+o6kthgxYgRcXV2xf/9+WX9/AWDXrl347bff0Lx5c5WcLi4uuHXrlsBkJbt48SICAwPV1m1sbJCSkiIgEb0tFqtEGiRJkvIX6dGjR/HZZ58BAOzs7PDo0SOR0dQUFhaioKBAbf3u3buoUKGCgERvlpCQgMaNG6ut6+vrIzs7W0CiktnZ2SE0NBQWFhYICQlBcHAwAODJkycwMDAQnK54Z8+exZkzZ5QfuOh/Ky4uDtu2bYOTk5PoKG+UmpoKS0tLtfXs7GzZFtkGBgbIzMxUW4+NjUWVKlUEJKK3xWKVSINcXV3h7+8Pd3d3nDp1CitXrgRQVGRZWVkJTqeqY8eOCAgIwM8//wwAUCgUePr0KXx9fdGlSxfB6Yrn4OCAqKgo2Nvbq6wfPHgQLi4uglIVb/z48ejXrx9MTExgb2+Ptm3bAgBOnz6t7GmWGzs7O0hacMzh9OnTb/U6OfWAAsAnn3yCmzdvakWx2qxZM+zfvx9jxowBAGWBGhQUhBYtWoiMVqIePXpg5syZ2Lp1K4CizImJiZgyZQp7xOVOdB8C0Yfk8uXLUr169SRTU1PJz89PuT569Gjp66+/FphM3b1796RatWpJH330kaSnpyc1b95cqlSpklS7dm3pwYMHouMVa+3atZKNjY0UHBwsGRsbS1u2bJH8/f2Vf5abixcvSjt27JCysrKUa/v27ZPOnj0rMFXJDh06JHXq1ElKSEgQHaVUL3s8i+v9lGsPqCRJ0o4dOyQXFxdp3bp1Unh4uHT58mWVLzk5d+6cVKFCBWnEiBGSgYGBNG7cOMnd3V0yNjaWwsPDRccrVkZGhtSyZUupYsWKkq6urmRnZyeVK1dOcnNzk54+fSo6HpWC0wCIZCA3Nxe6urooV66c6Cgqnj17huDgYERERKCwsBBNmjRBv379YGhoKDpaiYKCguDv74+kpCQARf1ofn5+GDJkiOBkpSsoKMCVK1dgb28Pc3Nz0XGKZW5ujpycHOTn58PIyEjt/fpyFJBolSpVQoUKFeDt7Y0BAwagcuXKxb7OzMxMw8lKp6OjPk1SoVBAkiQoFIpi23JEunLlChYsWKDy82Hy5MmyvTLw0vHjxxEZGanM7O7uLjoSvQGLVSINS09Px7Zt23Dr1i34+PjAwsICkZGRsLKygo2Njeh4Wis/Px+bN29G586dUbVqVTx69AiFhYXF9tXJwfjx41G/fn0MGTIEBQUFaNOmDc6fPw8jIyPs27dP2RYgJy/HFJVk4MCBGkpSuhcvXmDnzp1Yu3Ytzpw5gy5dumDIkCHw8PCQbT8lUDQurjSvt7cQfShYrBJpUHR0NDp06ICKFSvKfs7fhg0bULlyZXTt2hUA8O9//xs///wzXFxcsGXLFln+4jQyMsL169dlme11tra22LVrF1xdXbFr1y58++23OHHiBDZu3IgTJ07g3LlzoiOWCUlJSVi3bh02bNiA58+fY+DAgZgxYwb09Hhk458o7qASULQTrK+vL6uZ0a8KCwvDyZMni51ju2jRIkGp6E1YrBJpkLu7O5o0aYL58+ejQoUKuHz5MhwdHXH+/Hn07dsXt2/fFh1RqXbt2li5ciXat2+P0NBQdOjQAQEBAdi3bx/09PSwY8cO0RHVtGvXDuPGjYOXl5foKG9kYGCAmzdvwtbWFsOHD4eRkRECAgKQkJCAhg0bllgMaFpmZiZMTU2Vfy7Ny9fJUUJCAoYMGYJTp04hNTVVOTZMbm7duoWAgABcv34dCoUCH330EcaNG4eaNWuKjqZCR0en1F1qW1tbeHt7w9fXt9j2BhFmz56N6dOno3bt2rCyslLJr1AocPz4cYHpqDT8aEmkQdo05y8pKUl5KnnXrl344osvMHz4cLRs2VKWl6gBYNSoUfjuu+9w9+5dNG3aFMbGxirPN2jQQFAydVZWVrh27RqqVauGkJAQrFixAkDRnYF0dXUFp/ububk5kpOTYWlpiYoVKxZboMi1p/L58+fYvn071q5di9DQUHTt2hX79++XbaF66NAhdO/eHY0aNULLli0hSRLOnz+PunXrYu/evejYsaPoiErr16/HtGnT4O3tjY8//hiSJOHixYvYsGEDpk+fjtTUVCxYsAD6+vr4/vvvRccFACxZsgRr166Ft7e36Cj0jlisEmmQNs35MzExwePHj1G9enUcPnwYEyZMAFD03/Ds2TPB6YrXp08fAMDYsWOVa3I9oDJo0CD07t1bOfz9ZSHyxx9/oE6dOoLT/e348ePK4u7EiROC07ydsLAwrFu3DsHBwXBwcIC3tze2bt0q2yL1pSlTpmDChAkqN7R4uT558mRZFasbNmzAwoUL0bt3b+Va9+7dUb9+fQQGBuLYsWOoXr06Zs2aJZtiVUdHBy1bthQdg/4LbAMg0qDhw4cjNTVV+YszOjoaurq68PLygpubm6zuYNWvXz/ExMSgcePG2LJlCxITE1GpUiXs2bMH33//Pf7880/REdVo2wGVbdu2ISkpCV9++SVsbW0BFBUBFStWRI8ePQSn0146OjqoXr06Bg4ciKZNm5b4uu7du2sw1ZsZGBjgypUrcHZ2Vlm/ceMGGjRogNzcXEHJ1BkZGeHy5ctqWePi4tCwYUPk5OQgISEBdevWRU5OjqCUqubPn4/79+/L6ucsvR0Wq0QalJmZiS5duuDq1avIysqCtbU1UlJS0KJFCxw4cEDtsrVI6enpmD59OpKSkjBy5Eh4eHgAAHx9fVG+fHlMmzZNcMKyIzc3V7Z3rYqOjn7r18qlzeJteiTlttMOFN10YdGiRfjyyy9V1rdu3YpJkyYhMTFRUDJ1tWrVQs+ePYvdBd65cydiY2MRHh6OHj16yOb2zIWFhejatStu3LgBFxcXtdFrcuzDpyJsAyDSIFNTU5w9e1Yr5vxVrFgRy5cvV1ufMWOGgDRv503TFL755hsNJXmzgoICzJ49G6tWrcKDBw9w48YN5WSIGjVqyGYubKNGjZStFKWRU/H3+ilvbTFs2DAMHz4c8fHx+PTTT6FQKHD27FnMmzcP3333neh4KhYsWIAvv/wSBw8eRLNmzaBQKHDx4kVcv34d27dvB1DUo/+yNUcOxowZgxMnTqBdu3aoVKmSrMeYkSrurBJRidLT07FmzRqVk8lDhgyR3TD1l14fpp+Xl4ecnByUL18eRkZGshlaDwAzZ87Ehg0bMHPmTAwbNgx//vknHB0dsXXrVixevBihoaGiIwJ4c2vFq+TWZvH48WNUqlQJQNGBwaCgIOTm5qJbt25o3bq14HTqJElCQEAAFi5ciPv37wMArK2t4ePjg7Fjx8quuLpz5w5WrlyJGzduQJIk1KlTB//617+Qnp6ORo0aiY6npkKFCggODlaO4yPtwWKV6D1bunQphg8fDgMDAyxdurTU1756MEi08PBwdO7cGYaGhsrTvuHh4Xj27BkOHz6MJk2aiI74VuLi4jBy5Ej4+Pigc+fOouMoOTk5ITAwEB06dFAZYxYTE4MWLVrgyZMnoiNqrStXrqBbt25ISkqCs7MzgoOD4eHhgezsbOjo6CA7Oxvbtm2T9YizrKwsAEUFljZIT0/H5s2bsXbtWkRFRclml/1V9vb2OHTokKwOMNLbYbFK9J45ODggPDwclSpVgoODQ4mvUygUiI+P12Cy0rVu3RpOTk4ICgpSDlDPz8/H0KFDER8fj9OnTwtO+PbCw8PRv39/xMTEiI6iZGhoiJiYGNjb26sUq9euXcPHH3+Mp0+fio6oRlvaLDw9PaGnp4fJkyfjl19+wb59+9CpUyesXr0aQNHl4IiICFy4cEFwUu13/PhxrF27Fjt27IC9vT169eqFXr16oXHjxqKjqVm3bh1CQkKwbt06GBkZiY5D74DFKhEVy9DQEJcuXVLbhbh27RpcXV1lc8L3bVy6dAlt2rSRzaB9AHB1dcX48ePRv39/lWJ1xowZOHr0KM6cOSM6ohptabOoXLkyjh8/jgYNGuDp06cwNTVFWFgYXF1dAQAxMTFo3rw50tPTxQYF0KRJExw7dgzm5uZo3LhxqZf6IyMjNZisZHfv3sX69euxdu1aZGdno3fv3li1ahUuX74MFxcX0fFK1LhxY9y6dQuSJKFGjRpqB6zk8v0ldTxgRUTFMjU1RWJiolqxmpSUJNtLk3v27FF5LEkSkpOTsXz5ctnNV/T19cWAAQNw7949FBYWYseOHYiNjcXGjRuxb98+0fGKVVxrwqttFnKRlpaGqlWrAiiaF2xsbKwyY9Xc3Fx5mV20Hj16QF9fX/lnufWlvq5Lly44e/YsPvvsMyxbtgweHh7Q1dXFqlWrREd7Izm3fdAbSESkMb169ZLmzJmjtj5//nzpiy++EJCoZGPGjJFsbW2l4OBgKTExUUpKSpK2bNki2draSuPGjRMdr1gKhULlS0dHR7KyspK+/vpr6f79+6LjqQkJCZHc3NwkY2NjydDQUGrZsqV06NAh0bHe2cWLF6XatWuLjqGkUCikhw8fKh+bmJhI8fHxyscpKSmSjo6OiGhaT1dXV5owYYJ048YNlXU9PT3p6tWrglJRWcedVSINOnXqFHx9fdXWPTw8sGDBAgGJSrZgwQIoFAp88803yM/PBwCUK1cOI0eOVJutKBfaNrKoc+fOsjr09d/S1dVVnl6XC29vb+WOZW5uLkaMGKGcY/z8+XOR0Urk6OiIixcvKicYvJSeno4mTZrIoqf9zJkzWLt2LVxdXVGnTh0MGDBAVuOp3kZERIRywomLi4ss+2tJFXtWiTTI0NAQUVFRqF27tsr6yztFyfE2pjk5Oco+LycnJ606mFBQUIArV67A3t5erd9SLl68eIGHDx+qFdrVq1cXlKhkpbVZ2NnZ4eDBg4KSqRo0aNBbvW7dunXvOcm70dHRQUpKCiwtLVXWHzx4ADs7O7x48UJQMnU5OTkIDg7G2rVrERYWhoKCAixatAiDBw+WbZvQw4cP8dVXX+HkyZOoWLEiJElCRkYG2rVrh+DgYNnd8pr+xmKVSIOaNWuGbt264ccff1RZ9/Pzw969exERESEombqMjAwUFBSo3U89LS0Nenp6MDU1FZSsZOPHj0f9+vUxZMgQFBQUwM3NDaGhoTAyMsK+ffvQtm1b0RGV4uLiMHjwYJw/f15lXZIkWQ3Yf9Xrd4ZSKBSoUqUK2rdvj4ULF6JatWqCkmm3lx8CvLy8sGHDBpU5xgUFBTh27BiOHDmC2NhYURFLFRsbizVr1mDTpk1IT09Hx44d1T7YyEGfPn1w69YtbNq0CR999BGAogOjAwcOhJOTE7Zs2SI4IZWExSqRBu3Zswe9evVC37590b59ewDAsWPHsGXLFvz++++yOgDg6emJbt26YdSoUSrrq1atwp49e3DgwAFByUpma2uLXbt2wdXVFbt27cK3336LEydOYOPGjThx4gTOnTsnOqJSy5YtoaenhylTpqBatWpqB2saNmwoKBlp2ssPAcXdKaxcuXKoUaMGFi5ciM8++0xEvLdWUFCAvXv3Yu3atbIsVs3MzHD06FE0a9ZMZT0sLAydOnWSxXQIKh6LVSIN279/P2bPno2oqCgYGhqiQYMG8PX1RZs2bURHU2FhYYFz584pdyBeiomJQcuWLfH48WNByUpmYGCAmzdvwtbWFsOHD4eRkRECAgKQkJCAhg0bymp0lbGxMSIiIrR6QLk2tFloEwcHB1y8eBGVK1cWHaVMqlChAs6cOaN2dy05jrYjVTpvfgkR/S917doV586dQ3Z2Nh49eoTjx4/LrlAFig6hvDxY9aq8vDxZ9tYCgJWVFa5du4aCggKEhITA3d0dQFF/na6uruB0qlxcXPDo0SPRMd7J+PHjsWbNGgBQtlk0adIEdnZ2OHnypNhwZUBCQgIL1feoffv2GDdunMphwHv37mHChAno0KGDwGT0JixWiQR48eIF7t69i8TERJUvOWnWrBl+/vlntfVVq1ahadOmAhK92aBBg9C7d2/Uq1cPCoUCHTt2BAD88ccfstvBnDdvHv7973/j5MmTePz4MTIzM1W+5Gjbtm3K9oS9e/fi9u3biImJwfjx4zFt2jTB6bTf2LFji70l8/LlyzF+/HjNBypjli9fjqysLNSoUQM1a9aEk5MTHBwckJWVhWXLlomOR6VgGwCRBmnToZpz587B3d0dzZo1U+46HDt2DBcvXsThw4fRunVrwQmLt23bNiQlJeHLL7+Era0tAGDDhg2oWLEievToITjd317tU3yVHN8LL2lTm4U2srGxwZ49e9Q+DEZGRqJ79+64e/euoGRly5EjRxATEwNJkuDi4qK8AkPyxTmrRBrk7e0NPT097Nu3r9hDNXLSsmVLhIaG4qeffsLWrVuV/bVr1qyBs7Oz6Hgl+uKLL1Qep6enY+DAgYLSlOzEiROiI7yzl20W1apVQ0hICFasWAFAnm0W2ujx48cqkwBeMjU11bqWETnr2LGj8qoLaQcWq0QaFBUVpVWHaho1aoTNmzeLjvHW5s2bhxo1aiiHlPfu3Rvbt29HtWrVcODAATRo0EBwwr+1aNEC5cuXL/Y5uRYmL9ssXn7QknObhTZycnJCSEgIRo8erbJ+8OBBODo6CkpVdowdOxZOTk4YO3asyvry5ctx8+ZNBAQEiAlGb8RilUiDtOlQzZt6aOU4tD4wMBC//PILgKJLfUeOHMHBgwexdetWTJo0CYcPHxac8G+9e/fGjh071GaXPnjwAB06dMCff/4pKFnJ/Pz8UK9ePWWbxcs7ROnq6mLKlCmC02m/iRMnYvTo0UhNTVUZbbdw4UIWUv8D27dvL3ak1qeffoq5c+fyeyxj7Fkl0qDjx49j+vTpmD17NurXr49y5cqpPC+nQfs6OjqltinIsafS0NAQN27cgJ2dHcaNG4fc3FwEBgbixo0b+OSTT/DkyRPREZU++eQTuLi4qNxFKTk5Ge3bt0fdunWxbds2gelIlJUrV2LWrFnKE+s1atSAn58fvvnmG8HJtJ+BgQH+/PNPODk5qazfvHkT9erVQ25urqBk9CbcWSXSoJeN/K+PSZHjoZpLly6pPM7Ly8OlS5ewaNEizJo1S1Cq0pmbmyMpKQl2dnYICQmBv78/gKLvr5y+twBw4MABuLm5YcKECVi8eDHu3buH9u3bo2HDhggODhYdr0THjh3DsWPHir1F7Nq1awWlKjtGjhyJkSNHIjU1FYaGhjAxMREdqcxgm4X2YrFKpEHadKimuDsoubq6wtraGj/99BN69uwpIFXpevbsib59+8LZ2RmPHz+Gp6cngKJe4dd3U0SrVKkSDh06hFatWgEoullEkyZNsHnzZrXWALmYMWMGZs6cCVdXV9kfENR2vE/9/x7bLLQX2wCI6J3ExcWhUaNGyM7OFh1FTV5eHpYsWYKkpCR4e3ujcePGAICAgACYmJhg6NChghOqi4uLQ6tWrdCxY0ds2rRJ1gVgtWrVMH/+fAwYMEB0lDLpwYMHmDRpknLn+vVfz3K7OqCN2GahnVisEgmQk5ODxMREvHjxQmVdTqfVX5+ZKUkSkpOT4efnh5iYGERFRYkJpsXMzc2LLUZzcnKgr6+vMv4pLS1Nk9HeSqVKlRAWFoaaNWuKjlImeXp6IjExEaNHjy5251pOc4K1HdsstAuLVSINSk1NxaBBg3Dw4MFin5fTzklxB6wkSYKdnR2Cg4PRokULQclKt2nTJgQGBiI+Ph6hoaGwt7dHQEAAHBwchP+y37Bhw1u/Vo6zYSdPngwTExP88MMPoqOUSSXdu57+N9q3b48dO3agYsWKKuuZmZnw8vLC8ePHxQSjN2LPKpEGjR8/Hk+ePMGFCxfQrl077Ny5Ew8ePIC/vz8WLlwoOp6K1/trdXR0UKVKFTg5OUFPT54/OlauXIkff/wR48ePx6xZs5TFf8WKFREQECC8WJVjAfoucnNz8fPPP+Po0aNo0KCB2jSLRYsWCUpWNtjZ2ald+qf/nZMnT6pdzQKK3tdnzpwRkIjeFndWiTSoWrVq2L17Nz7++GOYmpoiPDwctWrVwp49ezB//nycPXtWdESt5uLigtmzZ8PLywsVKlTA5cuX4ejoiD///BNt27aV1YzbAwcOQFdXF507d1ZZP3z4MAoKCpSHw+SkXbt2pT6vTQcI5ejw4cNYuHAhAgMDUaNGDdFxyozo6GgARTc5OX78OCwsLJTPFRQUICQkBIGBgbh9+7aghPQm8tweISqjsrOzYWlpCQCwsLBAamoqatWqhfr16yMyMlJwOhQ7MLsk3bt3f49J/jsJCQnKQ1Wv0tfXl92BsClTpmDu3Llq64WFhZgyZYosi1UWo+9Xnz59kJOTg5o1a8LIyEht51qOfczaoFGjRlAoFFAoFMopAK8yNDTEsmXLBCSjt8VilUiDateujdjYWNSoUQONGjVS7qCsWrUK1apVEx0PXl5eb/U6uc2EfcnBwQFRUVGwt7dXWT948CBcXFwEpSpeXFxcsZnq1KmDmzdvCkhUsrcZU6ZQKLB9+3YNpCm7OD7p/UhISIAkSXB0dERYWJjKWLDy5cvD0tJS5XAjyQ+LVSINGj9+PJKTkwEAvr6+6Ny5MzZv3ozy5ctj/fr1YsMBakPetY2Pjw++/fZb5ObmQpIkhIWFYcuWLZgzZw5Wr14tOp4KMzMzxMfHq13uvXnzJoyNjcWEKoGZmZnoCB8Ebe9plquXH161/efbh4w9q0QC5eTkICYmBtWrV0flypVFxwFQdNjg6NGj+OyzzwAAU6dOxfPnz5XP6+npYebMmTAwMBAVsVRBQUHw9/dHUlISAMDGxgZ+fn4YMmSI4GSqhg8fjgsXLmDnzp3KUVA3b95Er1690KxZM9kV1/T+JSYmlvp89erVNZSkbNq4cWOpz3PWqnyxWCUiFYGBgdi3bx/27t0LoGicTt26dWFoaAgAiImJgY+PDyZOnCgyppr8/Hxs3rwZnTt3RtWqVfHo0SMUFhYqe4TlJiMjAx4eHggPD4etrS0A4O7du2jdunWx43Wo7CtuXNyr5Nh6o03Mzc1VHufl5SEnJwfly5eHkZERe4JljMUqkQYVFBRg/fr1Jd5bXQ5z/l7er/7zzz8HAJVT9QDwyy+/4P/+7/8QGhoqMmaxjIyMcP36dbWeVbmSJAlHjhzB5cuXYWhoiAYNGsDNzU10LBLk8uXLKo/z8vJw6dIlLFq0CLNmzZLlLY61XVxcHEaOHAkfHx+1yRwkHyxWiTRo9OjRWL9+Pbp27VrsHWoWL14sKNnfqlatimPHjqFu3boAiu5RfvHiRWVv5Y0bN9CsWTNkZGQITFm8du3aYdy4cW99UIxIG+zfvx8//fQTTp48KTpKmRQeHo7+/fsjJiZGdBQqAQ9YEWlQcHAwtm7dii5duoiOUqKMjAyVof+pqakqzxcWFqr0sMrJqFGj8N133+Hu3bto2rSp2kEl0bezXbp0KYYPHw4DAwMsXbq01NeOHTtWQ6lI7mrVqoWLFy+KjlFm6erq4v79+6JjUClYrBJpUPny5eHk5CQ6RqlsbW3x559/onbt2sU+Hx0dreyxlJs+ffoAUC30FAoFJEmSxbitxYsXo1+/fjAwMCh1F12hULBY/QBlZmaqPJYkCcnJyfDz84Ozs7OgVGXH63OkX35/ly9fjpYtWwpKRW+DbQBEGrRw4ULEx8dj+fLlpR6kEGncuHE4evQoIiIi1E78P3v2DK6urnB3d8eSJUsEJSzZnTt3Sn1eW3pZ6cNU3AErSZJgZ2eH4OBgtGjRQlCyskFHR0flsUKhQJUqVdC+fXssXLhQFrOuqXgsVok06PPPP8eJEydgYWGBunXrqt2hZseOHYKS/e3Bgwdo1KgRypcvj9GjR6NWrVpQKBSIiYnB8uXLkZ+fj0uXLsHKykp0VBVZWVm4cOEC8vLy8PHHH8tmFBjR2zp16pTKYx0dHVSpUgVOTk4qrTn0z6SmpkKhUPBnhBZhsUqkQYMGDSr1+XXr1mkoSekSEhIwcuRIHDlyBC9/RCgUCnTs2BErVqxQTgaQi+joaHh6eiIlJQWSJMHU1BTbtm2Du7u76Ggl0obJEKQZP/74I6ZMmQIjIyMAwJMnT9TGLNE/k56ejmnTpuG3337DkydPABSNsvrqq6/g7+/PUXEyx2KViEqUlpamvPWnk5MTLCwsBCcqXpcuXfDkyRMsXLgQBgYGmDFjBmJjY2V9ulcbJkOQZujq6iI5OVk5E9jU1BRRUVGy+1CordLS0tCiRQvcu3cP/fr1w0cffQRJknD9+nX8+uuvsLOzw/nz5/kBQcZYrBKR1rO0tMSBAwfg6uoKAHj8+DEsLS2RkZEBExMTwemKV7lyZWzcuFHWkyFIM3R0dJCSkqIsVl+fbUz/zPjx43Hs2DEcPXpUrX0pJSUFnTp1QocOHfgBUcbYBEOkQY0bNy72YJVCoYCBgQGcnJzg7e2Ndu3aCUinvR49eqRyK8pKlSrByMgIqampsi1WtWEyBFFZsGvXLgQGBhbbZ1+1alXMnz8fI0aMYLEqYzpvfgkR/a94eHggPj4exsbGaNeuHdq2bQsTExPcunULzZo1Q3JyMtzd3bF7927RUbWKQqFAVlYWMjMzkZmZiYyMDLW118cCifbdd99hyZIl4MUtevW9+vK9+/TpU5X3rtzev9okOTlZeZOT4tSrVw8pKSkaTETvim0ARBo0bNgwVK9eHT/88IPKur+/P+7cuYOgoCD4+vpi//79CA8PF5RS+5Q08uflmlzmrL5+u8zjx4/LejIEacbr799X37uvPhb9/tVWNjY2+O2339CqVatinz9z5gy++uor3Lt3T8PJ6G2xWCXSIDMzM0RERKhd/r158yaaNm2KjIwMxMTEoFmzZsjKyhKUUvu8PvKnJG3atHnPSUr3pmkQr5LLZAh6/7Tl/authgwZgps3b+LIkSMoX768ynPPnz9H586dUbNmTaxZs0ZQQnoT9qwSaZCBgQHOnz+vVqyeP39eOYC/sLAQ+vr6IuJpLW35Jb5u3TokJibC1tZWbUA5fbi05f2rrWbMmAFXV1c4Ozvj22+/RZ06dQAA165dw4oVK/D8+XNs2rRJcEoqDYtVIg0aM2YMRowYgYiICDRr1gwKhQJhYWFYvXo1vv/+ewDAoUOH0LhxY8FJtce79PKZmpq+xyRvx8HBQWVMEdGrbt26hXXr1uHWrVtYsmQJLC0tERISAjs7u1L7Lqlktra2CA0NxahRozB16lS12dHLly+HnZ2d4JRUGrYBEGnY5s2bsXz5csTGxgIAateujTFjxqBv374Aim5p+nI6AL1Zcf2qJZFDz9/rY4qIXjp16hQ8PT3RsmVLnD59GtevX4ejoyPmz5+PsLAwbNu2TXRErffkyRPExcUBkPfsaFLFYpWItNqr/X63b9/GlClT4O3trbyPemhoKDZs2IA5c+Zg4MCBomIqsVilkrRo0QJffvklJk6cqDJr9eLFi/Dy8uIBIPpgsVgl0rD09HRs27YN8fHxmDRpEiwsLBAZGQkrKyvY2NiIjqfVOnTogKFDh+Lrr79WWf/111/x888/4+TJk2KCvUJHRwf+/v5vnP86duxYDSUiuTAxMcGVK1fg4OCgUqzevn0bderUQW5uruiIREKwZ5VIg6Kjo+Hu7g4zMzPcvn0bQ4cOhYWFBXbu3Ik7d+5g48aNoiNqtdDQUKxatUpt3dXVFUOHDhWQqHirVq2Crq5uic8rFAoWqx+gihUrIjk5GQ4ODirrly5d4gdZ+qDxOCqRBk2cOBHe3t6Ii4tT6Un19PTE6dOnBSYrG+zs7IotVgMDA2V1gCI8PBwJCQklfsXHx4uOSAL07dsXkydPRkpKChQKBQoLC3Hu3DlMmjQJ33zzjeh4RMKwDYBIg8zMzBAZGYmaNWuqXOa7c+cOateuzct8/9CBAwfQq1cv1KxZE82bNwcAXLhwAbdu3cL27dvRpUsXwQkBXV1dTgOgYuXl5cHb2xvBwcGQJAl6enooKChA3759sX79+lJ344nKMrYBEGmQgYFBsaOWYmNjUaVKFQGJypYuXbogLi4OK1asQExMDCRJQo8ePTBixAjZ7Kxyf4BKUq5cOWzevBkzZ87EpUuXUFhYiMaNG8PZ2Vl0NCKhuLNKpEHDhw9Hamoqtm7dCgsLC0RHR0NXVxdeXl5wc3NDQECA6Ij0ns2YMQM+Pj4wMjISHYVk6sWLF0hISEDNmjWhp8c9JSIWq0QalJmZiS5duuDq1avIysqCtbU1UlJS0KJFCxw4cADGxsaiI2q99PR0rFmzBtevX4dCoYCLiwsGDx4MMzMz0dHUpKenIywsDA8fPkRhYaHKc+xR/PDk5ORgzJgx2LBhAwDgxo0bcHR0xNixY2FtbY0pU6YITkgkBotVIgGOHz+OyMhIFBYWokmTJnB3dxcdqUwIDw9H586dYWhoiI8//hiSJCE8PBzPnj3D4cOH0aRJE9ERlfbu3Yt+/fohOzsbFSpUULmxgUKhQFpamsB0JMK4ceNw7tw5BAQEwMPDA9HR0XB0dMSePXvg6+uLS5cuiY5IJASLVSINyc/Ph4GBAaKiolCvXj3Rccqk1q1bw8nJCUFBQcrLp/n5+Rg6dCji4+NlNXGhVq1a6NKlC2bPns2WAAIA2Nvb47fffkPz5s1VDmDevHkTTZo0eadbCxOVJWyGIdIQPT092Nvby+KWn2VVeHi4SqEKFH3f//3vf8PV1VVgMnX37t3D2LFjWaiSUmpqarFTIrKzs9/6lsJEZRHnrBJp0PTp0zF16lRe4n1PTE1NkZiYqLaelJSEChUqCEhUss6dOyM8PFx0DJKRZs2aYf/+/crHLwvUoKAg5e2DiT5E3Fkl0qClS5fi5s2bsLa2hr29vdqBqsjISEHJyoY+ffpgyJAhWLBgAT799FMoFAqcPXsWPj4+ardgFa1r167w8fHBtWvXUL9+fZQrV07l+e7duwtKRqLMmTMHHh4euHbtGvLz87FkyRJcvXoVoaGhOHXqlOh4RMKwZ5VIg2bMmAGFQlHirE1fX18NJypbXrx4AR8fH6xatQr5+fkAimZXjhw5EnPnzoW+vr7ghH/T0Sn5wpZCoWC7yAfqzz//xE8//YSIiAjlAczJkyejfv36oqMRCcNilUgDcnJy4OPjg127diEvLw8dOnTAsmXLULlyZdHRyqScnBzcunULkiTBycmJfaEke3l5eRg+fDh++OEHODo6io5DJCvsWSXSAF9fX6xfvx5du3bF119/jaNHj2LkyJGiY5VZRkZGMDc3R6VKlVioklYoV64cdu7cKToGkSxxZ5VIA2rWrIlZs2bhq6++AgCEhYWhZcuWyM3N5f2+/4cKCwvh7++PhQsX4unTpwCAChUq4LvvvsO0adNKvfSuCUuXLsXw4cNhYGCApUuXlvrasWPHaigVycWgQYNQv359TJw4UXQUIllhsUqkAeXLl0dCQgJsbGyUa4aGhrhx44Zs7llfFkydOhVr1qzBjBkz0LJlS0iShHPnzsHPzw/Dhg3DrFmzhOZzcHBAeHg4KlWqBAcHhxJfp1AoEB8fr8FkJAezZs3CggUL0KFDBzRt2lTtACY/wNCHisUqkQbo6uoiJSUFVapUUa5VqFAB0dHRpRYt9G6sra2xatUqtZP0u3fvxqhRo3Dv3j1ByYjejB9giIrH0VVEGiBJEry9vVVOo+fm5mLEiBEquyc7duwQEa/MSEtLQ506ddTW69SpI7vZttHR0WjQoEGxz+3atQteXl6aDUTCJSQkiI5AJEs8YEWkAQMHDoSlpSXMzMyUX/3794e1tbXKGv0zDRs2xPLly9XWly9fjoYNGwpIVLLOnTsXu1O2fft29OvXT0AiIiJ54s4qkQasW7dOdIQPwvz589G1a1ccPXoULVq0gEKhwPnz55GUlIQDBw6Ijqdi5MiR6NChA86fP49q1aoBAH777TcMHjwY69evFxuOhCjpYJVCoYCBgQGcnJzQo0cPWFhYaDgZkVjsWSWiMuX+/fv4v//7P8TExECSJLi4uGDUqFGwtrYWHU3NuHHjcPToUZw5cwYhISEYOnQoNm3ahF69eomORgK0a9cOkZGRKCgoQO3atSFJEuLi4qCrq4s6deogNjZWeVc2FxcX0XGJNIbFKhGRQAMGDMAff/yBe/fu4ddff0WPHj1ERyJBAgICcObMGaxbtw6mpqYAgMzMTAwZMgStWrXCsGHD0LdvXzx79gyHDh0SnJZIc1isEpFWi46OfuvXlnSgSVP27NmjtpaXl4cJEyagU6dOKlMMXp9oQGWfjY0Njhw5orZrevXqVXTq1An37t1DZGQkOnXqhEePHglKSaR5LFaJSKvp6OhAoVDgTT/KFAoFCgoKNJSqeG97UwI5ZCXNMzExwb59+9C2bVuV9ZMnT6Jbt27IyspCfHw8GjVqhMzMTDEhiQTgASsi0mraNO6nsLBQdASSsR49emDw4MFYuHAhmjVrBoVCgbCwMEyaNEk5yiwsLAy1atUSG5RIw7izSkRlxuPHj1GpUiUAQFJSEoKCgvDs2TN0794drVu3FpyuyB9//IG0tDR4enoq1zZu3AhfX19kZ2fDy8sLy5YtU5nJSx+Gp0+fYsKECdi4cSPy8/MBAHp6ehg4cCAWL14MY2NjREVFAQAaNWokLiiRhrFYJSKtd+XKFXTr1g1JSUlwdnZGcHAwPDw8kJ2dDR0dHWRnZ2Pbtm2yGLTv4eGBdu3aYfLkyQCKsjdp0gTe3t746KOP8NNPP+Ff//oX/Pz8xAYlYZ4+fYr4+HhIkoSaNWvCxMREdCQioVisEpHW8/T0hJ6eHiZPnoxffvkF+/btQ6dOnbB69WoAwJgxYxAREYELFy4ITgpUq1YNe/fuhaurKwBg2rRpOHXqFM6ePQsA+P333+Hr64tr166JjElEJBssVolI61WuXBnHjx9HgwYN8PTpU5iamiIsLExZEMbExKB58+ZIT08XGxSAgYEB4uLiYGdnBwBo1aoVPDw8MH36dADA7du3Ub9+fWRlZYmMSRrSs2dPrF+/HqampujZs2epr+XtmOlDxQNWRKT10tLSULVqVQBFJ6qNjY1V7vJjbm4um+LPysoKCQkJsLOzw4sXLxAZGYkZM2Yon8/KykK5cuUEJiRNMjMzg0KhUP6ZiNSxWCWiMuHlL/ySHsuFh4cHpkyZgnnz5mHXrl0wMjJSOfwVHR2NmjVrCkxImvTqrZh5W2ai4rFYJaIywdvbW3mCPjc3FyNGjICxsTEA4Pnz5yKjqfD390fPnj3Rpk0bmJiYYMOGDShfvrzy+bVr16JTp04CExIRyQt7VolI6w0aNOitXiennauMjAyYmJhAV1dXZT0tLQ0mJiYqBSyVXY0bN37rqwCRkZHvOQ2RPHFnlYi0npyK0LdVUn/iq722VPa9Ok4tNzcXK1asgIuLC1q0aAEAuHDhAq5evYpRo0YJSkgkHndWiYiIZGDo0KGoVq0a/vOf/6is+/r6IikpCWvXrhWUjEgsFqtEREQyYGZmhvDwcDg7O6usx8XFwdXVFRkZGYKSEYmlIzoAERERAYaGhsqbQ7zq7NmzMDAwEJCISB7Ys0pERCQD48ePx8iRIxEREYHmzZsDKOpZXbt2LX788UfB6YjEYRsAERGRTGzduhVLlizB9evXAQAfffQRxo0bh969ewtORiQOi1UiIiIiki32rBIREclEeno6Vq9eje+//x5paWkAiuar3rt3T3AyInHYs0pERCQD0dHRcHd3h5mZGW7fvo2hQ4fCwsICO3fuxJ07d7Bx40bREYmE4M4qERGRDEycOBHe3t6Ii4tTOf3v6emJ06dPC0xGJBaLVSIiIhm4ePEi/vWvf6mt29jYICUlRUAiInlgsUpERCQDBgYGyMzMVFuPjY1FlSpVBCQikgcWq0RERDLQo0cPzJw5E3l5eQAAhUKBxMRETJkyBb169RKcjkgcjq4iIiKSgczMTHTp0gVXr15FVlYWrK2tkZKSghYtWuDAgQMwNjYWHZFICBarREREMnLixAlERESgsLAQTZo0gbu7u+hIREKxWCUiIhLs999/x65du5CXlwd3d3cMHz5cdCQi2eCcVSIiIoF+/vlnjBgxAs7OzjAwMMD27duRkJCAOXPmiI5GJAvcWSUiIhKofv368PLywn/+8x8AwPr16zFmzBhkZWUJTkYkDyxWiYiIBDI2NsaVK1fg6OgIACgoKIChoSESExNRtWpVwemIxOPoKiIiIoGePXsGExMT5WNdXV3o6+sjJydHYCoi+WDPKhERkWCrV69WKVjz8/Oxfv16VK5cWbk2duxYEdGIhGMbABERkUA1atSAQqEo9TUKhQLx8fEaSkQkLyxWiYiIiEi22LNKREQkU+np6aIjEAnHYpWIiEgG5s2bh99++035+Msvv4SFhQVsbGxw+fJlgcmIxGKxSkREJAOBgYGws7MDABw5cgRHjx5FSEgIPD094ePjIzgdkTicBkBERCQDycnJymJ137596N27Nzp16oQaNWrgk08+EZyOSBzurBIREcmAubk5kpKSAAAhISFwd3cHAEiShIKCApHRiITizioREZEM9OzZE3379oWzszMeP34MT09PAEBUVBScnJwEpyMSh8UqERGRDCxevBg1atRAUlIS5s+fr7xJQHJyMkaNGiU4HZE4nLNKRERERLLFnlUiIiKZ2LRpE1q1agVra2vcuXMHABAQEIDdu3cLTkYkDotVIiIiGVi5ciUmTpwIT09PpKenKw9VVaxYEQEBAWLDEQnEYpWIiEgGli1bhqCgIEybNg26urrKdVdXV1y5ckVgMiKxWKwSERHJQEJCAho3bqy2rq+vj+zsbAGJiOSBxSoREZEMODg4ICoqSm394MGDcHFx0XwgIpng6CoiIiIZ8PHxwbfffovc3FxIkoSwsDBs2bIFc+bMwerVq0XHIxKGo6uIiIhkIigoCP7+/so7WdnY2MDPzw9DhgwRnIxIHBarREREMvPo0SMUFhbC0tJSdBQi4dizSkREJAPt27dHeno6AKBy5crKQjUzMxPt27cXmIxILO6sEhERyYCOjg5SUlLUdlMfPnwIGxsb5OXlCUpGJBYPWBEREQkUHR2t/PO1a9eQkpKifFxQUICQkBDY2NiIiEYkC9xZJSIiEkhHRwcKhQIAUNyvZENDQyxbtgyDBw/WdDQiWWCxSkREJNCdO3cgSRIcHR0RFhaGKlWqKJ8rX748LC0tVe5oRfShYbFKRERERLLFaQBEREQysWnTJrRs2RLW1ta4c+cOAGDx4sXYvXu34GRE4rBYJSIikoGVK1di4sSJ6NKlC9LT01FQUAAAMDc3R0BAgNhwRAKxWCUiIpKBZcuWISgoCNOmTVPpUXV1dcWVK1cEJiMSi8UqERGRDCQkJKBx48Zq6/r6+sjOzhaQiEgeWKwSERHJgIODA6KiotTWDx48CBcXF80HIpIJ3hSAiIhIBnx8fPDtt98iNzcXkiQhLCwMW7ZswZw5c7B69WrR8YiE4egqIiIimQgKCoK/vz+SkpIAADY2NvDz88OQIUMEJyMSh8UqERGRzDx69AiFhYWwtLQUHYVIOLYBEBERycjDhw8RGxsLhUIBhUKhckcrog8RD1gRERHJQGZmJgYMGABra2u0adMGbm5usLa2Rv/+/ZGRkSE6HpEwLFaJiIhkYOjQofjjjz+wf/9+pKenIyMjA/v27UN4eDiGDRsmOh6RMOxZJSIikgFjY2McOnQIrVq1Ulk/c+YMPDw8OGuVPljcWSUiIpKBSpUqwczMTG3dzMwM5ubmAhIRyQOLVSIiIhmYPn06Jk6ciOTkZOVaSkoKfHx88MMPPwhMRiQW2wCIiIgEady4MRQKhfJxXFwcnj9/jurVqwMAEhMToa+vD2dnZ0RGRoqKSSQUR1cREREJ4uXlJToCkexxZ5WIiIiIZIs9q0REREQkW2wDICIikoGCggIsXrwYW7duRWJiIl68eKHyfFpamqBkRGJxZ5WIiEgGZsyYgUWLFqF3797IyMjAxIkT0bNnT+jo6MDPz090PCJh2LNKREQkAzVr1sTSpUvRtWtXVKhQAVFRUcq1Cxcu4NdffxUdkUgI7qwSERHJQEpKCurXrw8AMDExQUZGBgDgs88+w/79+0VGIxKKxSoREZEM2NraKm8I4OTkhMOHDwMALl68CH19fZHRiIRisUpERCQDn3/+OY4dOwYAGDduHH744Qc4Ozvjm2++weDBgwWnIxKHPatEREQydOHCBZw/fx5OTk7o3r276DhEwrBYJSIiIiLZ4pxVIiIiQfbs2QNPT0+UK1cOe/bsKfW13F2lDxV3VomIiATR0dFBSkoKLC0toaNT8jEShUKBgoICDSYjkg8Wq0REREQkW2wDICIiEqywsBDr16/Hjh07cPv2bSgUCjg6OqJXr14YMGAAFAqF6IhEwnBnlYiISCBJktCtWzccOHAADRs2RJ06dSBJEq5fv44rV66ge/fu2LVrl+iYRMJwZ5WIiEig9evX4/Tp0zh27BjatWun8tzx48fh5eWFjRs34ptvvhGUkEgs7qwSEREJ1KlTJ7Rv3x5Tpkwp9vnZs2fj1KlTOHTokIaTEckD72BFREQkUHR0NDw8PEp83tPTE5cvX9ZgIiJ5YbFKREQkUFpaGqysrEp83srKCk+ePNFgIiJ5YbFKREQkUEFBAfT0Sj5Coquri/z8fA0mIpIXHrAiIiISSJIkeHt7Q19fv9jnnz9/ruFERPLCYpWIiEiggQMHvvE1nARAHzJOAyAiIiIi2WLPKhERERHJFotVIiIiIpItFqtEREREJFssVomIiIhItlisEhEREZFssVglIiIiItlisUpEREREssVilYiIiIhk6/8Bw2jSfKtN+7EAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(diabetes_df.corr(), cmap='Reds', annot=True)\n",
    "plt.title('Correlation Matrix');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Seperating Data and labels\n",
    "\n",
    "labels = diabetes_df.drop(columns = 'Outcome',axis = 1)\n",
    "target = diabetes_df['Outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>6</td>\n",
       "      <td>148</td>\n",
       "      <td>72</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.627</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>85</td>\n",
       "      <td>66</td>\n",
       "      <td>29</td>\n",
       "      <td>0</td>\n",
       "      <td>26.6</td>\n",
       "      <td>0.351</td>\n",
       "      <td>31</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            6      148             72             35        0  33.6   \n",
       "1            1       85             66             29        0  26.6   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  \n",
       "0                     0.627   50  \n",
       "1                     0.351   31  "
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "labels.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      1\n",
       "1      0\n",
       "2      1\n",
       "3      0\n",
       "4      1\n",
       "      ..\n",
       "763    0\n",
       "764    0\n",
       "765    0\n",
       "766    1\n",
       "767    0\n",
       "Name: Outcome, Length: 768, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "target"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Standardizing the data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Appling scaling using the StandardScaler class from `scikit-learn`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StandardScaler()"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scaler.fit(labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "standardized_data = scaler.transform(labels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.63994726,  0.84832379,  0.14964075, ...,  0.20401277,\n",
       "         0.46849198,  1.4259954 ],\n",
       "       [-0.84488505, -1.12339636, -0.16054575, ..., -0.68442195,\n",
       "        -0.36506078, -0.19067191],\n",
       "       [ 1.23388019,  1.94372388, -0.26394125, ..., -1.10325546,\n",
       "         0.60439732, -0.10558415],\n",
       "       ...,\n",
       "       [ 0.3429808 ,  0.00330087,  0.14964075, ..., -0.73518964,\n",
       "        -0.68519336, -0.27575966],\n",
       "       [-0.84488505,  0.1597866 , -0.47073225, ..., -0.24020459,\n",
       "        -0.37110101,  1.17073215],\n",
       "       [-0.84488505, -0.8730192 ,  0.04624525, ..., -0.20212881,\n",
       "        -0.47378505, -0.87137393]])"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "standardized_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels = standardized_data\n",
    "target=diabetes_df['Outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.63994726  0.84832379  0.14964075 ...  0.20401277  0.46849198\n",
      "   1.4259954 ]\n",
      " [-0.84488505 -1.12339636 -0.16054575 ... -0.68442195 -0.36506078\n",
      "  -0.19067191]\n",
      " [ 1.23388019  1.94372388 -0.26394125 ... -1.10325546  0.60439732\n",
      "  -0.10558415]\n",
      " ...\n",
      " [ 0.3429808   0.00330087  0.14964075 ... -0.73518964 -0.68519336\n",
      "  -0.27575966]\n",
      " [-0.84488505  0.1597866  -0.47073225 ... -0.24020459 -0.37110101\n",
      "   1.17073215]\n",
      " [-0.84488505 -0.8730192   0.04624525 ... -0.20212881 -0.47378505\n",
      "  -0.87137393]]\n",
      "0      1\n",
      "1      0\n",
      "2      1\n",
      "3      0\n",
      "4      1\n",
      "      ..\n",
      "763    0\n",
      "764    0\n",
      "765    0\n",
      "766    1\n",
      "767    0\n",
      "Name: Outcome, Length: 768, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(labels)\n",
    "print(target)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Splitting data into train test split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels_train,labels_test,target_train,target_test = train_test_split(labels,target,test_size = 0.2,stratify = target,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(768, 8) (614, 8) (154, 8)\n"
     ]
    }
   ],
   "source": [
    "print(labels.shape,labels_train.shape,labels_test.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Training the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "classifier = svm.SVC(kernel='linear') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC(kernel='linear')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# training the support vector machine classifier\n",
    "\n",
    "classifier.fit(labels_train,target_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finding accuracy score on the training data\n",
    "labels_train_prediction = classifier.predict(labels_train)\n",
    "training_data_accuracy = accuracy_score(labels_train_prediction,target_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The acuracy score of the training data:  0.7801302931596091\n"
     ]
    }
   ],
   "source": [
    "print(\"The acuracy score of the training data: \", training_data_accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finding accuracy score on the training data\n",
    "labels_test_prediction = classifier.predict(labels_test)\n",
    "test_data_accuracy = accuracy_score(labels_test_prediction,target_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The acuracy score of the text data:  0.7792207792207793\n"
     ]
    }
   ],
   "source": [
    "print(\"The acuracy score of the text data: \", test_data_accuracy)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The accuracy score for both the text data and training data is good this small amount of data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Making the predicting system to predict is a person is diabetic or not based on the information collected from the individual."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## *Predicting System*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is going to predict based on `0` and `1`\n",
    "\n",
    "* 0 > Not Diabetic\n",
    "* 1 > Diabetic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.04601433 -0.34096773  1.18359575 -1.28821221 -0.69289057  0.71168975\n",
      "  -0.5462679  -0.27575966]]\n"
     ]
    }
   ],
   "source": [
    "input_data = (4,110,92,0,0,37.6,0.291,30)\n",
    "\n",
    "# changin the input data to a numpy array\n",
    "\n",
    "input_data_as_numpy_array = np.asarray(input_data)\n",
    "\n",
    "# reshape the array as we are predicting for only one instance\n",
    "\n",
    "input_data_reshape = input_data_as_numpy_array.reshape(1,-1)\n",
    "\n",
    "# standardizing the input data\n",
    "std_data =  scaler.transform(input_data_reshape)\n",
    "\n",
    "print(std_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The prediction is : [0]\n",
      "Non-Diabetic\n"
     ]
    }
   ],
   "source": [
    "prediction = classifier.predict(std_data)\n",
    "\n",
    "print('The prediction is :', prediction)\n",
    "\n",
    "if prediction[0] == 0:\n",
    "    print(\"Non-Diabetic\")\n",
    "else:\n",
    "    (print(\"Diabetic\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### $THE-MODEL-PREDICTED-CORRECTLY$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Deployment on streamlit"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
