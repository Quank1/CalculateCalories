import ToolsCalculateCalories as tcc
import sys, os

sys.path.append(os.path.abspath('../LessonScraping'))

import sqltools


tcc.PrintProductsForFirstLetter(tcc.AskLetter())
tcc.GetCalories(tcc.AskWeight(sqltools.SearchProdyctForNum(tcc.WhoNumberProduct())))