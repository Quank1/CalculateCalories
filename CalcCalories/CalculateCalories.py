import ToolsCalculateCalories as tcc
import sys, os



sys.path.append(os.path.abspath('../CaloriesCalc'))

import sqltools


tcc.PrintProductsForFirstLetter(tcc.AskLetter())
tcc.GetCalories(tcc.AskWeight(sqltools.SearchProdyctForNum(tcc.WhoNumberProduct())))