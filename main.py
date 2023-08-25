{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from datetime import datetime\n",
    "from fastapi import FastAPI\n",
    "\n",
    "import uvicorn\n",
    "\n",
    "from sklearn.metrics.pairwise        import cosine_similarity\n",
    "from sklearn.utils.extmath           import randomized_svd\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise        import linear_kernel\n",
    "\n",
    "df = pd.read_csv('anime2.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.get(\"/Recomendacion/{variable}\")\n",
    "def Recomendacion(variable):\n",
    "    generos = df[df['tags'].apply(lambda x: all(tag in x for tag in variable))][['title', 'tags','rating','votes','description','eps','mediaType']]\n",
    "    return generos\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
