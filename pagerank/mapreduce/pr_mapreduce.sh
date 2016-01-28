#!/bin/bash

current_dir=$(cd `dirname $0`;pwd)
source ${current_dir}/g_conf.sh

idx=50;
current_task=pr_mapreduce
while [ $idx -lt 60 ]; do
    ((idx_out=$idx+1))
    OUTPUT_DIR="${BASE_DIR}/output_$idx_out"
    ${HADOOP_HOME}/bin/hadoop fs -rmr ${OUTPUT_DIR}
    ${HADOOP_HOME}/bin/hadoop streaming \
        -output ${OUTPUT_DIR} \
        -input ${BASE_DIR}/output_${idx} \
        -reducer "python/python/bin/python reduce-${current_task}.py" \
        -mapper "python/python/bin/python map-${current_task}.py" \
        -file "${current_dir}/map-${current_task}.py" \
        -file "${current_dir}/all_id_list" \
        -file "${current_dir}/reduce-${current_task}.py" \
        -jobconf mapred.job.name="${current_task}.wangbo01" \
        -jobconf mapred.job.map.capacity=100 \
        -jobconf stream.memory.limit=2400 \
        -jobconf mapred.job.reduce.capacity=100 \
        -jobconf mapred.reduce.tasks=100 \
        -jobconf mapred.job.priority=VERY_HIGH \
        -cacheArchive "${PYTHON_TOOL_DIR}#python"
    ret=$?
    if [ $ret -ne 0 ];then
        echo "error!!! $idx";
        exit 1
    fi
    ((idx=$idx+1))
done



