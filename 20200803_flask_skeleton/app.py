#non possiamo staccare questo paragraph
#se da err: bad file descriptor allora reset notebook
from flask import Flask, request, render_template

app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run

@app.route("/", methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    text = request.form.get('textarea')

    #ad ogni refresh
    #***l'html deve essere dentro la cartella templates per funzionare /content/templates/form1.html
    return render_template('form1.html',
                            AI_output=top_frequent(text, 10)[2:])

  else:
    #si parte con questa
    #***l'html deve essere dentro la cartella templates per funzionare /content/templates/form1.html

    return render_template('form1.html',
                           AI_output = '')

if __name__ == "__main__":
  app.run()