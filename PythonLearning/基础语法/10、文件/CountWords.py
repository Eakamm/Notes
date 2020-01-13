# '''
# @Author: Liu
# @Date: 2020-01-12 18:02:09
# @LastEditTime : 2020-01-12 18:10:00
# @LastEditors  : Please set LastEditors
# @Description: In User Settings Edit
# @FilePath: \VueLearnc:\Users\11346\OneDrive\笔记\PythonLearning\基础语法\10、文件\CountWords.py
# '''

def count_words(file_path):
  try:
    with open(file_path) as ani:
      text = ani.read()
  except FileNotFoundError:
    return '文件没有找到！'
  else:
    words = text.split()
    length = len(words)
    return "文章长度为："+str(length)