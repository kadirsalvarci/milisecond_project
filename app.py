from flask import Flask, render_template, request # ne gerekirse onu koyacaz 

app = Flask(__name__) #flask icin cati olusturuyoruz


def convert(millisecond): # this is milisecond code ... milisecon is gave by user 
    hour_in_millisecond = 60*60*1000 # 
    hours = millisecond // hour_in_millisecond #hours 
    millisecond_left = millisecond % hour_in_millisecond # left part 

    minute_in_millisecond = 60*1000
    minutes = millisecond_left // minute_in_millisecond
    millisecond_left %= minute_in_millisecond

    seconds = millisecond_left // 1000 #eger bolunmuyorsa  direk yazdirmam isteniyor
#asagida f string kullaniyoruz
    return f'{hours} hour/s '*(hours!=0) + f'{minutes} minute/s '*(minutes >0) + f'{seconds} second/s '*(seconds!=0) or f'just {millisecond} millisecond/s'
# return bizim yazdiracagimiz yeri gosteriyor. sifirdan farkli ise true doncek. sifirsa 0 donecek basilmayacak
@app.route('/', methods=['GET']) #dekoratif tanimlayacaz kontrol edicez 
def main_get():
        return render_template('index.html', developer_name ='Kadir', not_valid = False) #render template neresi istiyorsam oraya gonderiyor

@app.route('/', methods=['POST']) #input bitti artik post ile 
def main_post():
    alpha = request.form['number']#alpha string aldik ama cikista integar donecek
    if not alpha.isdecimal():
        return render_template('index.html', developer_name = 'Kadir', not_valid = True)
    if not (0 < int(alpha)):
        return render_template('index.html', developer_name = 'Kadir', not_valid = True)
    return render_template('result.html', developer_name=' Kadir', milliseconds = alpha, result = convert(int(alpha)) )
                         # ilk girilen sayi, result = convert(int(alpha))#fonksiyon icinde cikan sonuc  )  #fonksiyon icinde cikan sonuc 

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)