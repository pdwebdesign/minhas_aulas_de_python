import cherrypy
import datetime
class Ola(object):
        def index(self):
            return """<html>
                <head></head>
                <body>
                    <form method="get" action="/hoje">
                        <table>
                        <tr>
                            <td>Digite uma mensagem a ser apresentada:</td>
                            <td><input type="text" value=""  name="msg" /></td>
                        <tr>
                            <td>Digite um valor maior que zero:</td>
                            <td><input type="text" value="" name="val1"/></td>
                        <tr>
                        </table>
                        <button type="submit">Enviar</button>
                    </form>
                <body>
              </html>"""

        index.exposed = True

        def hoje(self,msg="",val1=0,show=False):
            val1 = int(val1)
            ret = msg + "," + str(datetime.datetime.today())
            if val1 > 0:
                ret += ",valor é maior que zero: " + str(val1)
            return ret

        hoje.exposed = True

cherrypy.quickstart(Ola())