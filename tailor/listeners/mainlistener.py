from swift.swiftlistener import SwiftListener
from utils.charformat import isUpperCamelCase

class MainListener(SwiftListener):

    def enterClassName(self, ctx):
        className = ctx.getText()
        if not isUpperCamelCase(className):
            print('Line', str(ctx.start.line) + ':', 'Class names should be in UpperCamelCase')