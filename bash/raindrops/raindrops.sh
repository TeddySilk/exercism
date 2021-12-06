#!/usr/bin/env bash

main () {
    output=""
    if [[ $(($@ % 3)) -eq 0 ]]
    then    
        output="${output}Pling"
    fi
    if [[ $(($@ % 5)) -eq 0 ]]
    then
        output="${output}Plang"
    fi
    if [[ $(($@ % 7)) -eq 0 ]]
    then
        output="${output}Plong"
    fi
    if [[ $output == "" ]]
    then
        output="$@"
    fi
    echo $output
}

main "$@"