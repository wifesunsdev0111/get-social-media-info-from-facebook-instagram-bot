from openai import OpenAI
client = OpenAI()

def summarize(description):
  # description = f'"Descoperă opulența și rafinamentul italian cu Setul Pietra Opulenta de la Italian Design. Acest ansamblu de 16 de piese, conceput pentru 4 persoane, te transportă în lumea luxului cu fiecare detaliu. Culoarea crem, îmbinată cu un aspect de piatră, adaugă un farmec distinct și autentic fiecărei mese.\nFiecare set include:\n4 boluri de 16 cm și 500 ml, cu un design elegant și o textură de piatră pentru a aduce o notă sofisticată fiecărui fel de mâncare.\n4 farfurii adânci de 21 cm și 500 ml, perfecte pentru a completa cu eleganță preparatele tale preferate.\n4 farfurii de desert de 20 cm, cu același aspect de piatră, aducând un strop de naturalețe și rafinament la fiecare moment dulce.\n4 farfurii întinse de 26 cm, cu o textură distinctivă, creând o atmosferă de lux în timpul fiecărui prânz sau cină.\nSetul Pietra Opulenta redefinește conceptul de lux în arta de a găti, oferind nu doar veselă, ci o experiență estetică autentic italiană. Realizat cu atenție la detalii și dedicat pasiunii pentru estetică, acest set adaugă o notă de sofisticare fiecărei mese. Bucură-te de fiecare moment într-un decor cu adevărat luxos, cu Setul Pietra Opulenta de la Italian Design."'

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": f"{description}\nremake this description with emot icons into romanian"}
    ]
  )

  print(response.choices[0].message.content)
  return response.choices[0].message.content
