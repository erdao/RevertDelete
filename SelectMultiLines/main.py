import sublime
import sublime_plugin

class SelectMultiLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_regions = []
        for sel_region in self.view.sel():
            sel_regions.append(sel_region)
        for sel_region in sel_regions:
            if not sel_region.empty():
            	lines=self.view.lines(sel_region)
            	lineStr=""
            	for line in lines:
            		curLine=self.view.substr(line)
            		#sublime.message_dialog(curLine)
            		newLine= ''+curLine[1:]
            		lineStr=lineStr+newLine+"\r\n"
            	self.view.replace(edit,sel_region,lineStr)