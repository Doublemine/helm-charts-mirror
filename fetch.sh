set -ex \
&& docker run --name fetch -v "${PWD}:/app" -e GIT_REPO=${GIT_REPO}  doublemine/helm-chart-fetcher:3.7\
&& git add . \
&& git commit -am "travis automated update helm charts " \
&& git checkout -B master \
&& git merge sync \
&& git push --force -u "https://$USERNAME:${GH_TOKEN}@${GH_REF}" master:master