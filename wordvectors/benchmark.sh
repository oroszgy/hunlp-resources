for dim in 100 150 300; do
    for min in  0 5 10; do 
        for cb in 0 1; do
            python -m gensim.scripts.word2vec_standalone -train $1 -output w2v_d${dim}_m${min}_c${min} -size ${dim} -threads 4 -min_count ${min} -cbow ${cb} -accuracy ./questions-words-hu.txt &> w2v_d${dim}_m${min}_c${min}.log
        done
    done
done
