import re
import os
import sys
import platform
import fleep


main_type = {
'IGNORE':[
'bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'icns', 'ico', 'ini', 'lnk', 'msi', 'sys', 'tmp'],

'AUDIO':[
'aif','cda','mid','idi','mp3','mpa','ogg','wav','wma','wpl',],

'PACKAGES':[
'7z', 
'arj', 'deb', 'pkg', 'rar', 'rpm', 'gz', 'z', 'zip'],

'DISC_IMAGE':[
'bin', 'dmg', 'iso', 'toast', 'vcd'],

'DATABASE':[
'csv', 'dat', 'db' ,'dbf', 'log', 'mdb', 'sav','sql', 'tar','xml'],

'EXECUTABLES':[ 
'apk', 'bat', 'bin', 'cgi', 'pl', 'com','exe', 'gadget', 'jar', 'py', 'wsf'],

'FONTS':[
'fnt', 'fon', 'otf', 'ttf'],

'IMAGES':[
 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff'],

'INTERNET_FILES':[
'asp','spx','cer','cfm','cgi','pl','css','htm', 'html','js','jsp','art','php','rss','xtml'],

'PRESENTATIONS':[
'odp', 'pps', 'ppt', 'pptx'],

'SOURCE_FILES':[
'c','class', 'cpp','cs','h','java', 'sh', 'swift', 'vb'],

'SPREAD_SHEETS':[
'ods', 'xlr', 'xls', 'xlsx'],

'VIDEOS':[
'3g2', '3gp', 'avi', 'flv', 'h264','m4v', 'mkv', 'mov','movie','mp4', 'mpg' ,'peg', 'rm', 'swf', 'vob', 'wmv'],

'DOCUMENTS':[
'ai','doc', 'docx', 'odt', 'pdf', 'rtf', 'tex', 'txt', 'wks', 'wp','swpd']}


MB = 1000000

class Cleano:

	os_type = str()
	desktop_path = str()
	documents_path = str()
	home_path = str()

	def __init__(self, home):
		''' Identify type of OS and set complete path of desktop. '''
		
		self.os_type  = platform.system()
		self.home_path = home
		self.desktop_path = os.path.join(home,'Desktop')
		
	def extension(self, path, filename):
		''' Find extension of file. If no extension, return as Miscellaneous type (misc). '''

		position = filename[::-1].find('.')
		
		if position==-1:
			with open(os.path.join(path, filename), 'rb') as file:
				info = fleep.get(file.read(128))
			if len(info.extension) > 1:
				return info.extension[0]
			else:
				return 'misc'

		else:
			extn = filename[-position:]
			return extn
	

	def clean_name(self, root, name):
		''' Replace spaces in filename by underscores. '''

		if name.find(' ') == -1:
			return name
		new_name = name.replace(' ','_');
		old_name = name.replace(' ','\ ');
		# print ('mv '+os.path.join(root,old_name)+' '+os.path.join(root,new_name))
		os.system('mv '+os.path.join(root,old_name)+' '+os.path.join(root,new_name))
		return new_name

	def list_files_and_directories(self,files, dirs, dir_path):
		''' Lists files and directories in a dir_path '''
		
		if os.path.isdir(dir_path)==False:
			sys.exit()

		temp  = os.listdir(dir_path)
		for f in temp:
			if os.path.isfile(os.path.join(dir_path, f)):
				files.append(f)
			else:
				dirs.append(f)

	def determine_main_type(self, ex):
		''' Determines type of file given extension. '''
		
		type_ = ''
		
		for main in main_type:
			if ex in main_type[main]:
				type_ = main+'/'
				if os.path.isdir(os.path.join(self.documents_path, type_)) == False:
					os.system('mkdir '+os.path.join(self.documents_path,type_))
				break

		return type_



# public:

	def clean_desktop(self,desktop_path):
		''' Catagorizes files in Desktop and puts them in folders in Documents folder. '''

		self.desktop_path = desktop_path
		self.documents_path = desktop_path.rstrip('Desktop')+'Documents'

		files = list()
		dirs = list()

		if self.os_type=='Linux':
			
			self.list_files_and_directories(files,dirs,self.desktop_path)	

			valid_files = map(lambda x: self.clean_name(self.desktop_path,x),filter(lambda x: re.match('^[^\.].*[^~]$',x)!=None , files))
			valid_dirs = filter(lambda x: re.match('^[^\._]',x)!=None , dirs)
			
			file_extn = [(filename, self.extension(self.desktop_path,filename)) for filename in valid_files]
			# print(file_extn)

			for file_tuple in file_extn:

				if file_tuple[1] in main_type['IGNORE']:
					continue

			# determine file type, prepend to extn
				type_ = self.determine_main_type(file_tuple[1]) 

				extn = type_ +'_'+file_tuple[1].upper()+'_'
				
				# print (file_tuple, extn)
				
				if os.path.isdir(os.path.join(self.documents_path,extn))==False:

					os.system('mkdir '+os.path.join(self.documents_path,extn))

				os.system('mv '+os.path.join(self.desktop_path,file_tuple[0])+' '+os.path.join(self.documents_path,extn))

	def large_files(self):
		''' Prints top 10 large files in each directory starting from root'''

		for root, files, dirs in os.walk(self.home):
			
			cur_dir = root
			print ('#####################################################')
			print ('Directory: ',cur_dir)
			print('******************* TOP 10 LARGE FILES ***************')
			file_sizes = [(filename, os.path.getsize(os.path.join(cur_dir, filename))) for filename in files]
			top_10_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)[:10]
			for f in top_10_files:
				print(f[0], f[1]/MB,'MB')
			print('*******************************************************')
