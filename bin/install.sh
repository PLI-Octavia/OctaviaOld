#!/bin/bash

if [ -z "${BRANCH_NAME}" ]
then
	if [ -d .git ]
	then
		BRANCH_NAME=`git rev-parse --abbrev-ref HEAD`
		if [ "${BRANCH_NAME}" == "HEAD" ]
		then
			BRANCH_NAME=`git branch --remote --verbose --no-abbrev --contains | sed -rne 's/^[^\/]*\/([^\ ]+).*$/\1/p'`
		fi
	fi
fi
if [ ! -z "${BRANCH_NAME}" ]
then
	export BRANCH=${BRANCH_NAME}
fi

echo "${GIT_LOCAL_BRANCH}"
echo "${BRANCH_NAME}"
