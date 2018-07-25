from flask import abort
from flask import Flask
from flask import render_template
from flask import request

import itertools
import subprocess


app = Flask(__name__)


def get_words(strs, find_len=None):
    result = []
    len_str = len(strs)
    start = 3
    end = len_str + 1
    if find_len:
        start = int(find_len)
        end = start + 1
    for n in range(start, end):
        result.append('------ %d ------' % n)
        result_n = set()
        for indicates in itertools.permutations(strs, n):
            find_str = ''.join(indicates)
            try:
                output = subprocess.check_output('sdcv -n {0} | grep -i "\-\->{0}"'.format(find_str), shell=True)
                res = output.strip().decode('utf-8')
                if len(res) > 3:
                    f_reses = res.split('\n')
                    for f_res in f_reses:
                        if len(f_res[3:]) == n:
                            # print '**********', f_res[3:]
                            result_n.add(f_res[3:].upper())
            except:
                pass

        for r in result_n:
            result.append(r)
    return result


@app.route('/', methods=['GET', 'POST'])
def first_page():
    results = []
    if request.method == 'POST':
        words = request.form.get('words')
        if any(s.isdigit() for s in words):
            return abort(400)
        results = get_words(words)
    return render_template('example.html', results=results)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

