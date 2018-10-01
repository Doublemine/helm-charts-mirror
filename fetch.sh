set -ex \
&& python fetch.py \
&& git add . \
&& git commit -am "travis automated update helm charts " \
&& git checkout -B master \
&& git merge sync \
&& git push --force -u "https://$USERNAME:${GH_TOKEN}@${GH_REF}" master:master