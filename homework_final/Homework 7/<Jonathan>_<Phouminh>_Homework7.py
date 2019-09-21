#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Jonathan Phouminh
# CSCI 1200
# HOMEWORK 7
# GRADE REPORT
# PARTNER: AUSTIN ROWEN


def print_name(file_two,first_name,last_name,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
    '''Takes the parameters described above and if the returned values and if any of those are true from the has_trouble function then the if statement will make the program write in the new txt'''
    if has_concerning(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war) or has_trouble(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
        file_two.write('Student name: '+ first_name+' '+last_name + '\n')
        
def print_warning(file_two,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
    '''Takes the parameters described above and if the returned values and if any of those are true from the has_trouble function then the if statement will make the program write in the new txt'''
    if has_concerning(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war)==True:
        file_two.write('\tConcerning Courses:' '\n')
        
def print_trouble(file_two,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
    '''Takes the parameters described above and if the returned values and if any of those are true from the has_trouble function then the if statement will make the program write in the new txt'''
    if has_trouble(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war)==True:
        file_two.write('\tTrouble Courses: ' + '\n')
    
def has_concerning(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
    '''Takes the parameters described above and compares then with boolean values and returns another boolean value'''
    if concern(math_cur,math_obj,math_war)=='warning':
        return True
    elif concern(engl_cur,engl_obj,engl_war)=='warning':
        return True
    elif concern(hist_cur,hist_obj,hist_war)=='warning':
        return True
    elif concern(sci_cur,sci_obj,sci_war)=='warning':
        return True
    elif concern(lang_cur,lang_obj,lang_war)=='warning':
        return True
    else:
        return False


def has_trouble(math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war):
    '''Takes the parameters described above and compares then with boolean values and returns another boolean value'''
    if concern(math_cur,math_obj,math_war)=='trouble':
        return True
    elif concern(engl_cur,engl_obj,engl_war)=='trouble':
        return True
    elif concern(hist_cur,hist_obj,hist_war)=='trouble':
        return True
    elif concern(sci_cur,sci_obj,sci_war)=='trouble':
        return True
    elif concern(lang_cur,lang_obj,lang_war)=='trouble':
        return True
    else:
        return False

def concern(cur,obj,war):
    '''Takes the parameters above and compares the int value of current and with int values of warning and objective grades and returns the string values of the boolean statements'''
    if int(cur)<=int(obj):
       return 'trouble'
        
    elif int(cur)<=int(war):
        return 'warning'
    else:
        return 'false'

def math_class_warning(file_two,concern,cur,obj,war):
     '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
     if  concern=='warning':
        file_two.write('\t\tCurrent Math grade:'+cur+', Warning Math grade:'+war + '\n')
def math_class_trouble(file_two,concern,cur,obj,war):
     '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
     if concern=='trouble':
        file_two.write('\t\tCurrent Math grade:'+cur+', Objective Math grade:'+obj + '\n')

    
    
def eng_class_warning(file_two,concern,cur,obj,war):
    '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='warning':
        file_two.write('\t\tCurrent English grade:'+cur+', Warning English grade:'+war + '\n')

def eng_class_trouble(file_two,concern,cur,obj,war):
    '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='trouble':
       file_two.write('\t\tCurrent English grade:'+cur+', Objective English grade:'+obj + '\n')

    

    
def hist_class_warning(file_two,concern,cur,obj,war):
    '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='warning':
        file_two.write('\t\tCurrent History grade:'+cur+', Warning History grade:'+war + '\n')

def hist_class_trouble(file_two,concern,cur,obj,war):
    '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='trouble':
        file_two.write('\t\tCurrent History grade:'+cur+', Objective History grade:'+obj + '\n')

    
    
def sci_class_warning(file_two,concern,cur,obj,war):
     '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
     if concern=='warning':
       file_two.write('\t\tCurrent Science grade:'+cur+', Warning Science grade:'+war + '\n')

def sci_class_trouble(file_two,concern,cur,obj,war):
    '''Takes the parameters above and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='trouble':
       file_two.write('\t\tCurrent Science grade:'+cur+', Objective Science grade:'+obj + '\n')


def lang_class_warning(file_two,concern,cur,obj,war):
    '''takes the two argmuents objective and compares the string with warning as a boolean value and if it true then it will write in the new txt file'''
    if concern=='warning':
        file_two.write('\t\tCurrent Language grade:'+cur+', Warning Language grade:'+ war + '\n')
def lang_class_trouble(file_two,concern,cur,obj,war):
    '''Takes the parameters file_two, concern, cur, obj, war and compares the current grade with the string trouble and if it is true then it will write into the new txt file'''
    if concern=='trouble':
        file_two.write('\t\tCurrent Language grade:'+cur+', Objective Language grade:'+ obj + '\n')

def main():
    '''This function opens a text file that the program will read from and and opens a new file which allows the program to write a new txt in the same directory'''
    file_one=open('student_files.csv','r')
    file_two=open('file_grades_report.txt','w')
    y=file_one.readlines()
    del y[0]    #deletes first line of the grade file because it wont be read
    for line in y:
        z=line.split(',')
        last_name=z[0]
        first_name=z[1]
        math_cur=z[2]
        math_obj=z[3]
        math_war=z[4]
        engl_cur=z[5]
        engl_obj=z[6]
        engl_war=z[7]
        hist_cur=z[8]
        hist_obj=z[9]
        hist_war=z[10]
        sci_cur=z[11]
        sci_obj=z[12]
        sci_war=z[13]
        lang_cur=z[14]
        lang_obj=z[15]
        lang_war=z[16]
        print_name(file_two,first_name,last_name,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war)
        print_warning(file_two,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war)
        math_class_warning(file_two,concern(math_cur,math_obj,math_war),math_cur,math_obj,math_war)
        eng_class_warning(file_two,concern(engl_cur,engl_obj,engl_war),engl_cur,engl_obj,engl_war)
        hist_class_warning(file_two,concern(hist_cur,hist_obj,hist_war),hist_cur,hist_obj,hist_war)
        sci_class_warning(file_two,concern(sci_cur,sci_obj,sci_war),sci_cur,sci_obj,sci_war)
        lang_class_warning(file_two,concern(lang_cur,lang_obj,lang_war),lang_cur,lang_obj,lang_war)
        print_trouble(file_two,math_cur,math_obj,math_war,engl_cur,engl_obj,engl_war,hist_cur,hist_obj,hist_war,sci_cur,sci_obj,sci_war,lang_cur,lang_obj,lang_war)
        math_class_trouble(file_two,concern(math_cur,math_obj,math_war),math_cur,math_obj,math_war)
        eng_class_trouble(file_two,concern(engl_cur,engl_obj,engl_war),engl_cur,engl_obj,engl_war)
        hist_class_trouble(file_two,concern(hist_cur,hist_obj,hist_war),hist_cur,hist_obj,hist_war)
        sci_class_trouble(file_two,concern(sci_cur,sci_obj,sci_war),sci_cur,sci_obj,sci_war)
        lang_class_trouble(file_two,concern(lang_cur,lang_obj,lang_war),lang_cur,lang_obj,lang_war)
        
        
        

        
    file_one.close()
    file_two.close()
if __name__ == '__main__':
    main()