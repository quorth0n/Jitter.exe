#Thanks to YingaTech for the following commands: "burrtio", "lmgtfy", "rickroll", and "xkcd"

from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import subprocess

class BurritoPlugin(WillPlugin):
    @respond_to("^guinness")
    def guinness(self, message):
        """guinness, irish, or beer: gives Liam the memories..."""
        self.say("(greenbeer)(greenbeer)(greenbeer) *starts singing in drunk irish accent* (greenbeer)(greenbeer)(greenbeer)", message=message)
        #self.say("(greenbeer)(greenbeer)(greenbeer)<i>Here we go again...</i>(greenbeer)(greenbeer)(greenbeer)<br><iframe width=\"420\" height=\"315\" src=\"https://www.youtube.com/embed/-Jgma--0WYU\" frameborder=\"0\" allowfullscreen></iframe>", message=message)
    @respond_to("^irish")
    def irish(self, message):
        self.say("(greenbeer)(greenbeer)(greenbeer) *starts singing in drunk irish accent* (greenbeer)(greenbeer)(greenbeer)", message=message)
    @respond_to("^beer")
    def beer(self, message):
        self.say("(greenbeer)(greenbeer)(greenbeer) *starts singing in drunk irish accent* (greenbeer)(greenbeer)(greenbeer)", message=message)
    @respond_to("^burrito")
    def burrito(self, message):
        """burrito: Show a burrito"""
        self.say("<img src=\"http://carlosandgabbysbrooklyn.com/images/chicken%20burrito.jpg\">", html=True, message=message)
    @respond_to("^lmgtfy me (?P<query>.*)")
    def lmgtfy(self,message,query):
        """lmgtfy me _____: Open a letmegooglethatforyou link with the designated search - useful with a :P"""
        self.reply(message, "http://lmgtfy.com/?q="+query)
    @respond_to("^rickroll")
    def rickroll(self, message):
        """rickroll: Rickroll everyone"""
        self.say("https://www.youtube.com/watch?v=dQw4w9WgXcQ", message=message)
    @respond_to("^xkcd me (?P<name>.*)")
    def xkcd(self,message,name):
        """xkcd me _____: Show an XKCD comic"""
        name=repr(message).split("<body>xkcd me ")[1].split("</body>")[0]
        self.reply(message, subprocess.Popen("php -r \"echo explode(\\\"\\\\n\\\",explode(\\\"Image URL (for hotlinking/embedding): \\\",file_get_contents(\\\"http://xkcd.com/"+name+"\\\"))[1])[0];\" 2>&1", shell=True, stdout=subprocess.PIPE).stdout.read())
