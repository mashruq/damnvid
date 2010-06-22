# -*- coding: utf-8 -*-
import os, sys
import time
import traceback
from dCore import *

class DamnLog:
	def __init__(self, logpath=None, stderr=True, flush=False, handleerrors=True):
		DamnLog.instance = self
		self.time = 0
		self.streams = []
		self.autoflush = flush
		if logpath is not None:
			try:
				if not os.path.exists(os.path.dirname(logpath)):
					os.makedirs(os.path.dirname(logpath))
				f = DamnOpenFile(logpath, 'wb')
				self.streams.append(f)
				f.write((self.getPrefix() + u'Log opened.').encode('utf8'))
			except:
				try:
					print 'Warning: Couldn\'t open log file!'
					traceback.print_exc()
				except:
					pass
		if stderr:
			self.streams.append(sys.stdout)
		if handleerrors:
			try:
				sys.excepthook = self.logException
			except:
				self.log('!! Cannot override excepthook. This looks bad.')
	def getPrefix(self):
		t = int(time.time())
		if self.time != t:
			self.time = t
			return u'[' + DamnUnicode(time.strftime('%H:%M:%S')) + u'] '
		return u''
	def write(self, message):
		message = u'\r\n' + (self.getPrefix() + DamnUnicode(message.strip())).strip()
		for s in self.streams:
			try:
				print >> s, message.encode('utf8'),
			except:
				try:
					print 'Could not print to stream', s,'message:', message.strip()
				except:
					pass
		if self.autoflush:
			self.flush()
	def log(self, *args):
		import dCore
		s = []
		for i in args:
			s.append(dCore.DamnUnicode(i))
		return self.write(u' '.join(s))
	def logException(self, typ, value, tb):
		import traceback
		import dCore
		import dLog
		try:
			info = traceback.format_exception(typ, value, tb)
			e = []
			for i in info:
				e.append(dCore.DamnUnicode(i).strip())
			self.log('!!',u'\n'.join(e))
		except:
			try:
				self.log('!! Error while logging exception. Something is very wrong.')
			except:
				pass # Something is very, very wrong.
	def flush(self):
		for s in self.streams:
			try:
				s.flush()
			except:
				pass
			try:
				os.fsync(s)
			except:
				pass
	def close(self):
		self.log('Closing log.')
		for s in self.streams:
			if s != sys.stderr:
				try:
					s.close()
				except:
					pass
def Damnlog(*args):
	if DamnLog.__dict__.has_key('instance'):
		return DamnLog.instance.log(*args)
	return None
