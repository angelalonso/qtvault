#!/usr/bin/env bash

UNLOCKED="yes"
PASS="some something somes same somelier"
SECRET="some1 something1 somes1 same1 somelier1"

sleep 1

if [[ "${1}" != "" ]] ; then
  case "$1" in
    unlocked)
      echo "${UNLOCKED}";;
    pass)
      echo "${PASS}";;
    secret)
      echo "${SECRET}";;
    *)
      echo "invalid";;
  esac
else
  echo "nothing"
fi
