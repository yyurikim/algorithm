def solution(video_len, pos, op_start, op_end, commands):
    def cvt_int(ipt):
        return int(ipt.replace(':', ''))
    
    op_start_num = cvt_int(op_start)
    op_end_num = cvt_int(op_end)
    cur_time = pos

    for i in range(len(commands)):
        if op_start_num <= cvt_int(cur_time) < op_end_num:
            cur_time = op_end
        answer = [cur_time[0:2], cur_time[-2:]]
        if commands[i] == 'next':
            answer[1] = str(int(answer[1]) + 10)
            if int(answer[1]) >=60:
                answer[0] = str(int(answer[0]) + 1)
                answer[1] = str(int(answer[1]) - 60)

        elif commands[i] == 'prev':
            answer[1] = int(answer[1]) - 10
            if int(answer[1]) < 0:
                answer[0] = str(int(answer[0]) - 1)
                answer[1] = str(int(answer[1]) + 60)
                if int(answer[0]) < 0:
                    answer[0] = '00'
                    answer[1] = '00'
            else:
                answer[1] = str(answer[1])
        
        answer[0] = answer[0].zfill(2)
        answer[1] = answer[1].zfill(2)
            
        cur_time = ':'.join(answer)
        
        if op_start_num <= cvt_int(cur_time) < op_end_num:
            cur_time = op_end
        elif cvt_int(cur_time) > cvt_int(video_len):
            cur_time = video_len
        else:   
            cur_time = ':'.join(answer)
        

    return cur_time
