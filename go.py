# cd "C:\Program Files (x86)\Google\Chrome\Application" && chrome.exe --remote-debugging-port=9222

import time
import os
import psutil

if 'chrome.exe' not in (p.name() for p in psutil.process_iter()):
	os.startfile('.\\run_chrome.bat')
	time.sleep(5)

time.sleep(1)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-num_threads", default = 4)
args = parser.parse_args()
num_threads = int(args.num_threads)

import pychrome
import threading
import queue
import math
import tqdm
import sys

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

js = """
function toDataURL(url, callback) {
	var xhr = new XMLHttpRequest()
	xhr.onload = function() {
		var reader = new FileReader()
		reader.onloadend = function() {
			callback(reader.result)
		}
		reader.readAsDataURL(xhr.response)
	}
	xhr.open('GET', url)
	xhr.responseType = 'blob'
	xhr.send()
}
window.count = 0
document.querySelectorAll('<removed-due-to-legal-reasons>').forEach((t) => {
	t.querySelectorAll('li').forEach((t) => {
		var img = ''
		try {
			img = t.querySelector('<removed-due-to-legal-reasons>').style.backgroundImage.replace(/^.*https/, 'https').replace('\")', '')
		} catch(e) {
		}
		if (img) {
			window.count += 1
			toDataURL(img, function(dataUrl) {
				t.querySelector('<removed-due-to-legal-reasons>').style.backgroundImage = 'url(' + dataUrl + ')'
				window.count -= 1
				console.log(window.count)
			})
		}
	})
})
"""

js2 = """
document.querySelectorAll('<removed-due-to-legal-reasons>').forEach((t) => {
	go += '<hr>'
	t.querySelectorAll('li').forEach((t) => {
		var name = ''
		var price = ''
		var desc = ''
		var img = ''
		try {
			name = t.querySelector('<removed-due-to-legal-reasons>').innerHTML
		} catch (e) {
		}
		try {
			price = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replace(/<span .*$/, '')
		} catch (e) {
		}
		try {
			desc = t.querySelector('<removed-due-to-legal-reasons>').innerHTML
		} catch (e) {
		}
		try {
			img = t.querySelector('<removed-due-to-legal-reasons>').style.backgroundImage.replace('url(', '').replace(')', '').replaceAll('\"', '')
		} catch (e) {
		}
		go += '<table><tr><td><img src=' + img + '></td><td><table><tr><td>' + name + '</td></tr><tr><td>' + price + '</td></tr><tr><td>' + desc + '</td></tr></table></td></tr></table>'
	})
})
go
"""

js3 = """
var go = true

var p = []
document.querySelectorAll('<removed-due-to-legal-reasons>').forEach((t) => {
	t.querySelectorAll('li').forEach((t) => {
		if (t.querySelector('<removed-due-to-legal-reasons>')) {
			p.push(t.querySelector('<removed-due-to-legal-reasons>').style.backgroundImage.replace(/^.*https/, 'https').replace('\")', ''))
		}
	})
})

j = 0
l = 999999
for (var i = 0; i < p.length; i++) {
	if (p[i] == 'https://<removed-due-to-legal-reasons>/img/logo-simple-ys.svg') {
		j += 1
		l = i
	}
}

if (j == 0) {
	go = false
} else {
	go = true
	if (((j == 1) || (j == 3 && window.location.href == '<removed-due-to-legal-reasons>') || (j == 2 && window.location.href == '<removed-due-to-legal-reasons>') || (j == 3 && window.location.href == '<removed-due-to-legal-reasons>')) && l < p.length - 1) {
		go = false
		window.fix = true
	}
}

String(go)
"""

js4 = """
var go = ''
var arr = []
document.querySelectorAll('<removed-due-to-legal-reasons>').forEach((t) => {
	t.querySelectorAll('li').forEach((t) => {
		if (t.querySelector('<removed-due-to-legal-reasons>') && t.querySelector('<removed-due-to-legal-reasons>').style.backgroundImage.replace(/^.*https/, 'https').replace('\")', '') == 'https://<removed-due-to-legal-reasons>/img/logo-simple-ys.svg') {
			arr.push(t)
		}
	})
})
arr.forEach((t) => {
	go += ' | ' + t.querySelector('<removed-due-to-legal-reasons>').innerHTML
})
document.title = String(arr.length)
go
"""

js5 = """
if (((window.fix == true && window.count == 1) || (window.fix == true && window.count == 3 && window.location.href == '<removed-due-to-legal-reasons>') || (window.fix == true && window.count == 2 && window.location.href == '<removed-due-to-legal-reasons>') || (window.fix == true && window.count == 3 && window.location.href == '<removed-due-to-legal-reasons>'))) {'0'} else {'-1'}
"""

js6 = """
<script>

function checkVisible(e) {
	var rect = e.getBoundingClientRect();
	if (rect.top == 0 && rect.bottom == 0) { return false }
	if ((rect.top > 0 && rect.bottom > 0) || (rect.top < 0 && rect.bottom < 0)) {
		return false
	}
	var t2 = e.querySelectorAll('table')[0]
	var t = t2.querySelector('span > a')
	console.log(t.innerHTML, rect.top, rect.bottom, t2.clientHeight)
	return true
}

function scrolled() {
	document.querySelectorAll('.r').forEach((e)=>{
		if (checkVisible(e, i)) {
			e.querySelectorAll('table')[0].style = "position:fixed; top:0px; background-color: white; width: 100%"
		} else {
			e.querySelectorAll('table')[0].style = "position:static; width: 100%"
		}
	})	
}

function sta() {
	document.querySelectorAll('.r').forEach((e)=>{
		e.querySelectorAll('table')[0].style = "position:static; width: 100%"
	})
}
function scrolll(t) {
	sta()
	var b = []
	var i = 0
	var j = 0
	document.querySelectorAll(".n").forEach((c) => {
		if (c.parentNode.parentNode.parentNode.parentNode.parentNode.style.display == 'block') {
			i += 1
			b.push(c.parentNode.parentNode.querySelector("td:nth-child(5) > span"))
			if (t == c) {
				j = i
			}
		}
	})
	b[j].scrollIntoView()
}
function scrolll2(t) {
	sta()
	var b = []
	var i = 0
	var j = 0
	document.querySelectorAll(".p").forEach((c) => {
		if (c.parentNode.parentNode.parentNode.parentNode.parentNode.style.display == 'block') {
			i += 1
			b.push(c.parentNode.parentNode.querySelector("td:nth-child(5) > span"))
			if (t == c) {
				j = i
			}
		}
	})
	b[j - 2].scrollIntoView()
	scrolled()
}

var i = 0
document.querySelectorAll('span').forEach((e)=>{i += 1; e.innerHTML = '<a target="_blank" href="' + document.querySelector('.dataframe > tbody > tr:nth-child(' + i + ') > td:nth-child(7) > a').href + '">' + e.innerHTML + '</a>'})

document.addEventListener("scroll", (e)=>{
	scrolled()
})

var i = 1;
document.querySelectorAll('.dataframe > tbody > tr').forEach((e)=>{
    e.querySelector('th').innerHTML = '<input id="' + i + '" type="checkbox" checked>'
    i++
})

function check_apply() {
    sta()
	document.querySelectorAll('input[type="checkbox"]').forEach((e)=>{
        var who = parseInt(e.id)
        var checked = e.checked
        var i = 0
        document.querySelectorAll('.r').forEach((r)=>{
            i++
            if (i == who) {
                if (!checked) {
                    r.style.display = 'none'
                    r.style.visibility = 'hidden'
                } else {
                    r.style.display = 'block'
                    r.style.visibility = 'visible'
                }
            }
        })
	})
}

function toggle() {
	document.querySelectorAll('input[type="checkbox"]').forEach((e)=>{
		if (e.checked) {
			e.checked = false
		} else {
			e.checked = true
		}
	})
    sta()
	document.querySelectorAll('input[type="checkbox"]').forEach((e)=>{
        var who = parseInt(e.id)
        var checked = e.checked
        var i = 0
        document.querySelectorAll('.r').forEach((r)=>{
            i++
            if (i == who) {
                if (!checked) {
                    r.style.display = 'none'
                    r.style.visibility = 'hidden'
                } else {
                    r.style.display = 'block'
                    r.style.visibility = 'visible'
                }
            }
        })
	})
}

function apply() {

	var err = false

	var min_score = 0
	var max_score = 0
	var min_review = 0
	var max_review = 0
	var min_min = 0
	var max_min = 0

	try {
		min_score = parseFloat(document.querySelector('#min_score').value)
		max_score = parseFloat(document.querySelector('#max_score').value)
		min_review = parseFloat(document.querySelector('#min_review').value)
		max_review = parseFloat(document.querySelector('#max_review').value)
		min_min = parseFloat(document.querySelector('#min_min').value)
		max_min = parseFloat(document.querySelector('#max_min').value)
	} catch (e) {
		err = true
	}

	if (!err) {

		document.querySelectorAll('.dataframe > tbody > tr').forEach((e)=>{
	    
	    	var cb = e.querySelector('input[type="checkbox"]')
	    
			score = parseFloat(e.querySelector('td:nth-child(3)').innerText)
			review = parseFloat(e.querySelector('td:nth-child(4)').innerText)
			min = parseFloat(e.querySelector('td:nth-child(5)').innerText)

			if (min_score <= score && score <= max_score && min_review <= review && review <= max_review && min_min <= min && min <= max_min) {
				cb.checked = true
			} else {
				cb.checked = false
			}
	 
		})

		document.querySelectorAll('input[type="checkbox"]').forEach((e)=>{
	        var who = parseInt(e.id)
	        var checked = e.checked
	        var i = 0
	        document.querySelectorAll('.r').forEach((r)=>{
	            i++
	            if (i == who) {
	                if (!checked) {
	                    r.style.display = 'none'
	                    r.style.visibility = 'hidden'
	                } else {
	                    r.style.display = 'block'
	                    r.style.visibility = 'visible'
	                }
	            }
	        })
		})

	}

}

document.querySelector('#filter').querySelectorAll('input[type="text"]').forEach((e)=>{
	e.addEventListener('input', (event) => {
		//apply()
	})
})

function scrl(x) {
	var b
	var i = 0
	document.querySelectorAll(".r").forEach((c) => {
		i += 1
		if (i == x) {
			b = c.querySelector("table:nth-child(3) > tbody > tr > td:nth-child(1) > button.n")
		}
	})
	b.scrollIntoView()
}
var i = 0
document.querySelectorAll('.dataframe > tbody > tr').forEach((e)=>{
	e.querySelectorAll('td:nth-child(2)').forEach((e)=>{
		i += 1
		e.innerHTML = '<a href="javascript:scrl(' + i + ');">' + e.innerHTML + '</a>'
	})
})

document.querySelectorAll('button.p').forEach((e)=>{
	var b = document.createElement('button')
	b.innerHTML = 'Top'
	b.setAttribute('onclick', 'javascript:window.scrollTo(0, 0)')
	e.parentNode.appendChild(b)
})

function clean() {
	var arr = []
	var i = 0
	document.querySelectorAll('.r').forEach((r) => {
	    if (r.style.visibility == 'hidden') {
	    	arr.push(i)
	    }
	    i++
	})
	for (var j = arr.length - 1; j >= 0; j--) {
		document.querySelectorAll('.r')[arr[j]].remove()
	}
}

</script>
"""

def run(tab, e, w = False, s = False):
	print('\n\nrun: ' + e + '\n\n')
	r = tab.Runtime.evaluate(expression = e)
	if w:
		tab.wait(10)
	if s:
		time.sleep(1)
	return r.get('result').get('value')

def wait(tab, w, h):
	print('\n\nwait: ' + w + ' != ' + h + '\n\n')
	while tab.Runtime.evaluate(expression = w).get('result').get('value') != h:
		time.sleep(1)

def wait2(tab, w):
	print('\n\nwait2: ' + w + ' == ""\n\n')
	tt = tab.Runtime.evaluate(expression = w).get('result').get('value')
	while tt == '' or tt == None:
		tt = tab.Runtime.evaluate(expression = w).get('result').get('value')
		time.sleep(1)

def wait3(tab, w):
	print('\n\nwait3: ' + w + ' == "0"\n\n')
	while tab.Runtime.evaluate(expression = w).get('result').get('value') == '0':
		time.sleep(1)

def wait4(tab, w, h):
	print('\n\nwait4: ' + w + ' == ' + h + '\n\n')
	while tab.Runtime.evaluate(expression = w).get('result').get('value') == h:
		time.sleep(1)

browser = pychrome.Browser(url = 'http://127.0.0.1:9222')

tab = browser.new_tab()
tab.start()
tab.Network.enable()
tab.Page.enable()
tab.Page.navigate(url = 'https://www.<removed-due-to-legal-reasons>/restaurants/new?lat=<lat>&lng=<lng>&vertical=restaurants&sort=rating_desc', _timeout = 10)
tab.wait(3)

num_sonuc = '<removed-due-to-legal-reasons>'
sel_rest = '<removed-due-to-legal-reasons>'
sel_rest_c = '<removed-due-to-legal-reasons>'
sel_rest_g = '<removed-due-to-legal-reasons>'

wait2(tab, "document.querySelector('" + num_sonuc + "').innerHTML")
run(tab, "document.querySelector('body').style.filter = 'blur(5px)'")

tt = run(tab, "document.querySelector('" + num_sonuc + "').innerHTML")
print("["+tt+']')
le = int(tt.split(' ')[0])

print(str(le))
cur = int(run(tab, "document.querySelectorAll('" + sel_rest + "').length"))
cur2 = int(run(tab, "document.querySelectorAll('" + sel_rest_c + "').length"))
cur3 = int(run(tab, "document.querySelectorAll('" + sel_rest_g + "').length"))
i = 0
j = 1
last = 0
last2 = 0
last3 = 0
while cur + cur2 + cur3 < le - 1:
	run(tab, 'window.scrollBy(0, 600)')
	cur = int(run(tab, "document.querySelectorAll('" + sel_rest + "').length"))
	cur2 = int(run(tab, "document.querySelectorAll('" + sel_rest_c + "').length"))
	cur3 = int(run(tab, "document.querySelectorAll('" + sel_rest_g + "').length"))
	print('\t' + str(cur) + ' + ' + str(cur2) + ' + ' + str(cur3) + ' = ' + str(cur + cur2 + cur3) + ' -> ' + str(le))
	time.sleep(0.05)
	if last == cur or last2 == cur2 or last3 == cur3:
		i = i + 1
		if i == 10 * j:
			print('top')
			run(tab, 'window.scrollTo(0, 0)')
			i = 0
			j = j + 1
	elif last != cur:
		last = cur
	elif last2 != cur2:
		last2 = cur2
	elif last3 != cur3:
		last3 = cur3
cur = int(run(tab, "document.querySelectorAll('" + sel_rest + "').length"))
cur2 = int(run(tab, "document.querySelectorAll('" + sel_rest_c + "').length"))
cur3 = int(run(tab, "document.querySelectorAll('" + sel_rest_g + "').length"))
print('\n' + str(cur) + ' + ' + str(cur2) + ' + ' + str(cur3) + ' = ' + str(cur + cur2 + cur3))

def browse(m, args, q):

	tab = None

	for i in args:

		n = 'cache/' + i[0].replace('https://www.<removed-due-to-legal-reasons>/restaurant/', '').replace('/', '_') + '.html'

		if not os.path.exists(n):

			if tab == None:
				tab = browser.new_tab()
				tab.start()
				tab.Network.enable()
				tab.Page.enable()

			tab.Page.navigate(url = i[0], _timeout = 10)
			tab.wait(2)

			go = ''
			while go == '':

				wait3(tab, "document.querySelectorAll('<removed-due-to-legal-reasons>').length")
				run(tab, "document.querySelector('body').style.filter = 'blur(5px)'")
				wait3(tab, "var t = document.querySelectorAll('<removed-due-to-legal-reasons>'); t[t.length - 1].querySelectorAll('li').length")
				wait2(tab, "var t = document.querySelectorAll('<removed-due-to-legal-reasons>'); var p = t[t.length - 1].querySelectorAll('li'); p[p.length - 1].querySelector('<removed-due-to-legal-reasons>').innerHTML")

				rem_c = 0

				while run(tab, js3.replace('\t', '').replace('\n', ';')) == 'true':
					time.sleep(1)
					run(tab, "if(window.ttt){clearInterval(window.ttt)}; if(document.body.scrollHeight - 300 <= window.scrollY + window.innerHeight){window.scrollTo(0, 0)}; window.ttt = setInterval(()=>{if(document.body.scrollHeight - 300 <= window.scrollY + window.innerHeight){clearInterval(window.ttt)}else{window.scrollBy(0, 400)}}, 300)")

					rems = run(tab, js4.replace('\t', '').replace('\n', ';'))
					print(rems)
					if '|' in rems and 8 >= len(rems.split('|')) and len(rems.split('|')) >= 3:
						rem_c += 1
						if rem_c == 4 or run(tab, "var t = document.querySelectorAll('<removed-due-to-legal-reasons>'); if (t) {var p = t[0].querySelectorAll('li'); if (p) {p[0].querySelector('<removed-due-to-legal-reasons>')}}") == '':
							rem_c = 0
							print('\n\n_________RELOAD_________\n\n')
							tab.Page.navigate(url = i[0], _timeout = 10)
							tab.wait(2)
							wait3(tab, "document.querySelectorAll('<removed-due-to-legal-reasons>').length")
							run(tab, "document.querySelector('body').style.filter = 'blur(5px)'")
							wait3(tab, "var t = document.querySelectorAll('<removed-due-to-legal-reasons>'); t[t.length - 1].querySelectorAll('li').length")
							wait2(tab, "var t = document.querySelectorAll('<removed-due-to-legal-reasons>'); var p = t[t.length - 1].querySelectorAll('li'); p[p.length - 1].querySelector('<removed-due-to-legal-reasons>').innerHTML")

				run(tab, js.replace('\t', '').replace('\n', ';'))
				time.sleep(1)
				while run(tab, "String(window.count)") != '0' and run(tab, js5) != '0':
					time.sleep(1)

				go = run(tab, "var go = '<div style=\"display: block\" class=\"r\"><hr><hr><table style=\"width: 100%\"><tr><td><button class=\"n\" type=\"button\" onclick=\"scrolll(this)\">Next</button><button class=\"p\" type=\"button\" onclick=\"scrolll2(this)\">Prev</button></td><td></td><td></td><td></td><td><span>" + i[1].replace("'", "").replace('"', '') + "</span></td><td>(score: " + str(i[2]) + ", reviews: " + str(i[3]) + ", min: " + str(i[4]) + "TL, delivery: " + str(i[5]) + "TL)</td></tr></table>'; " + js2.replace('\t', '').replace('\n', ';')) + '</div>'

			with open(n, 'w', encoding = 'utf-8') as f:
				f.write(go)

			a = q.get()
			a = a + 1
			q.put(a)
			with tqdm.trange(m, file = sys.stdout) as progress_bar:
				progress_bar.reset()
				progress_bar.update(a)

		else:

			a = q.get()
			a = a + 1
			q.put(a)
			with tqdm.trange(m, file = sys.stdout) as progress_bar:
				progress_bar.reset()
				progress_bar.update(a)

	if tab != None:
		tab.stop()
		browser.close_tab(tab)

urls = []
names = []
scores = []
reviews = []
mins = []
deliveries = []
print('\n')

for i in run(tab, "var go = ''; document.querySelectorAll('<removed-due-to-legal-reasons>').forEach((t) => {var link = t.querySelector('a').href; var name = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replaceAll('&amp;', '&'); var scor = t.querySelector('<removed-due-to-legal-reasons>').innerHTML; var numr = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replaceAll('(', '').replaceAll(')', '').replaceAll('+', ''); var mini = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replaceAll(' minimum', '').replaceAll('TL', '').replaceAll('.', ''); if (!parseFloat(mini)) {mini = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replaceAll(' minimum', '').replaceAll('TL', '').replaceAll('.', '')}; var deli = t.querySelector('<removed-due-to-legal-reasons>').innerHTML.replaceAll(',', '.').replaceAll('TL', '').replaceAll('Ücretsiz', '0'); go += '||' + link + '|' + name + '|' + scor + '|' + numr + '|' + mini + '|' + deli; }); go").split('||'):
	t = i.split('|')
	if len(t) == 6:
		print('* ' + t[0] + ', ' + t[1] + ', ' + t[2] + ', ' + t[3] + ', ' + t[4] + ', ' + t[5])
		print('\n')
		urls.append(t[0])
		names.append(t[1])
		scores.append(float(t[2]))
		reviews.append(int(t[3]))
		mins.append(int(t[4]))
		deliveries.append(float(t[5]))
	else:
		print('! ' + i + '\n')

df = pd.DataFrame({
	'names': names,
	'scores': scores,
	'reviews': reviews,
	'mins': mins,
	'deliveries': deliveries,
	'urls': urls
})

df = df.reset_index(drop = True)
df = df.sort_values(by = ['scores', 'reviews'], ascending = [False, False])
print(df)

go = []
t = []
j = 0
k = 0
for i in df.urls:
	t.append([i, df.names[k], df.scores[k], df.reviews[k], df.mins[k], df.deliveries[k]])
	j = j + 1
	k = k + 1
	if j == math.ceil(len(df.urls) / num_threads):
		j = 0
		go.append(t)
		t = []
if len(t) != 0:
	go.append(t)

que = queue.Queue()
que.put(0)

ts = []
for i in go:
	ts.append(threading.Thread(target = browse, args=(len(df.urls), i, que)))
for i in ts:
	i.start()
for i in ts:
    i.join()

df.to_html('df.html', render_links = True, encoding = 'utf-8', index = True)
html = ''
with open('df.html', 'r', encoding = 'utf-8') as f:
	html = f.read()

with open('go.html', 'w', encoding = 'utf-8') as f:
	f.write('<style>body { font-family: Arial, Helvetica, sans-serif } table { font-size: 97% } .dataframe { width: 100% } .dataframe td:nth-child(3) { text-align: end } .dataframe td:nth-child(4) { text-align: end } .dataframe td:nth-child(5) { text-align: end } .dataframe td:nth-child(6) { text-align: end }</style><table id="filter"><tr><td><input size=1 type="text" id="min_score" value="0.0"></td><td><=</td><td>scores</td><td><=</td><td><input size=1 type="text" id="max_score" value="5.0"></td><td>,</td><td><input size=2 type="text" id="min_review" value="0"></td><td><=</td><td>reviews</td><td><=</td><td><input size=2 type="text" id="max_review" value="99999"></td><td>,</td><td><input size=2 type="text" id="min_min" value="0"></td><td><=</td><td>mins</td><td><=</td><td><input size=2 type="text" id="max_min" value="99999"></td><td><button onclick="apply()" style="margin-left: 20px">Filter</button></td></tr></table><button onclick="toggle()">Toggle</button>')
	f.write('<button onclick="check_apply()">Apply</button>')
	f.write('<button onclick="this.disabled=true; clean()">Clean for print</button>')
	f.write(html)
	f.write('<button onclick="check_apply()">Apply</button>')
	for i in df.urls:
		with open('cache/' + i.replace('https://www.<removed-due-to-legal-reasons>/restaurant/', '').replace('/', '_') + '.html', 'r', encoding = 'utf-8') as f2:
			f.write(f2.read())
	f.write(js6)

print(df)

tab.Page.navigate(url = 'file:///C:/Users/ukaza/Downloads/yemek/go.html', _timeout = 10)
tab.stop()
