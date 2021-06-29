import os
import argparse
import gol
import time as ts


def fixed_encoding(tab, file_cnf):

    file_handler = open(file_cnf,'r').read()
    for i_bit in range(10,0,-1):
        file_handler = file_handler.replace('%d '%(i_bit),'%dx '%(tab[i_bit-1]))

    file_handler = file_handler.replace('x','')

    return file_handler

def transition_encoding(i_grid, size,  file_cnf):

    variables_tab = [0,0,0,0,0,0,0,0,i_grid-size*size,i_grid ]

    # var_tab
    # 0 1 2
    # 3 8 4
    # 5 6 7

    # state
    #  1  2  3  4  5
    #  6  7  8  9 10
    # 11 12 13 14 15
    # 16 17 18 19 20
    # 21 22 23 24 25

    # all border cases
    # topline
    if (i_grid-1) % (size*size) < size:
        # 1
        if i_grid % (size*size) == 1:
            variables_tab[0] = i_grid - 1
            variables_tab[1] = i_grid - size
            variables_tab[2] = i_grid - size + 1
            variables_tab[3] = i_grid - size*size + size-1
            variables_tab[4] = i_grid - size*size + 1
            variables_tab[5] = i_grid - size*size + size*2-1
            variables_tab[6] = i_grid - size*size + size
            variables_tab[7] = i_grid - size*size + size + 1
        # 5
        elif i_grid % (size*size) == size:
            variables_tab[0] = i_grid - size - 1
            variables_tab[1] = i_grid - size
            variables_tab[2] = i_grid - size*2 + 1
            variables_tab[3] = i_grid - size*size - 1
            variables_tab[4] = i_grid - size*size - size + 1
            variables_tab[5] = i_grid - size*size + size - 1
            variables_tab[6] = i_grid - size*size + size
            variables_tab[7] = i_grid - size*size +1
        # 2 3 4
        else:
            variables_tab[0] = i_grid - size - 1
            variables_tab[1] = i_grid - size
            variables_tab[2] = i_grid - size + 1
            variables_tab[3] = i_grid - size*size - 1
            variables_tab[4] = i_grid - size*size + 1
            variables_tab[5] = i_grid - size*size + size - 1
            variables_tab[6] = i_grid - size*size + size
            variables_tab[7] = i_grid - size*size + size + 1
    # bottom line
    elif (i_grid-1) % (size*size) >= size*(size-1):
        # 21
        if i_grid % (size*size) == size*(size-1) +1 :
            variables_tab[0] = i_grid - size*size - 1
            variables_tab[1] = i_grid - size*size - size
            variables_tab[2] = i_grid - size*size - size + 1
            variables_tab[3] = i_grid - size*size + size - 1
            variables_tab[4] = i_grid - size*size + 1
            variables_tab[5] = i_grid - size*size + size - 1 - size*(size-1)
            variables_tab[6] = i_grid - size*size - size*(size-1)
            variables_tab[7] = i_grid - size*size - size*(size-1) + 1
        # 25
        elif i_grid % (size*size) == 0:
            variables_tab[0] = i_grid - size*size - size -  1
            variables_tab[1] = i_grid - size*size - size
            variables_tab[2] = i_grid - size*size - size*2 + 1
            variables_tab[3] = i_grid - size*size - 1
            variables_tab[4] = i_grid - size*size - size +  1
            variables_tab[5] = i_grid - size*size - size*(size-1) -1
            variables_tab[6] = i_grid - size*size - size*(size-1)
            variables_tab[7] = i_grid - size*size*2 + 1
        # 22 23 24
        else:
            variables_tab[0] = i_grid - size*size - size - 1
            variables_tab[1] = i_grid - size*size - size
            variables_tab[2] = i_grid - size*size - size + 1
            variables_tab[3] = i_grid - size*size - 1
            variables_tab[4] = i_grid - size*size + 1
            variables_tab[5] = i_grid - size*size - size*(size-1) -1
            variables_tab[6] = i_grid - size*size - size*(size-1)
            variables_tab[7] = i_grid - size*size - size*(size-1) + 1
    # 6 11 16
    elif i_grid % size == 1:
            variables_tab[0] = i_grid - size*size - 1
            variables_tab[1] = i_grid - size*size - size
            variables_tab[2] = i_grid - size*size - size + 1
            variables_tab[3] = i_grid - size*size + size - 1
            variables_tab[4] = i_grid - size*size + 1
            variables_tab[5] = i_grid - size*size + size*2 -1
            variables_tab[6] = i_grid - size*size + size
            variables_tab[7] = i_grid - size*size + size + 1
    # 10 15 20
    elif i_grid % size == 0:
            variables_tab[0] = i_grid - size*size - size - 1
            variables_tab[1] = i_grid - size*size - size
            variables_tab[2] = i_grid - size*size - size*2 + 1
            variables_tab[3] = i_grid - size*size - 1
            variables_tab[4] = i_grid - size*size - size + 1
            variables_tab[5] = i_grid - size*size + size - 1
            variables_tab[6] = i_grid - size*size + size
            variables_tab[7] = i_grid - size*size + 1
    # all inside
    else:
        variables_tab[0] = i_grid - size*size - size - 1
        variables_tab[1] = i_grid - size*size - size
        variables_tab[2] = i_grid - size*size - size + 1
        variables_tab[3] = i_grid - size*size - 1
        variables_tab[4] = i_grid - size*size  + 1
        variables_tab[5] = i_grid - size*size + size - 1
        variables_tab[6] = i_grid - size*size + size
        variables_tab[7] = i_grid - size*size + size + 1

    assert(0 not in variables_tab)

    return fixed_encoding(tab = variables_tab, file_cnf = file_cnf)

def grid_over_time(size, time, file_cnf):

    nr_of_variables = size*size*(time+1)

    file_handler = open(file_cnf,'r').readlines()
    nr_of_clauses = len(file_handler)*size*size*time

    encoding = ''
    for i_time in range(1, time+1):
        for i_grid in range(1, size*size+1):
            encoding += transition_encoding(size*size*i_time+i_grid,size, file_cnf)


    return nr_of_variables, nr_of_clauses, encoding

def read_output_value(file_in):

    file_handler = open(file_in,'r').readlines()
    size = int(file_handler[0].strip())
    time = int(file_handler[1].strip())
    value_tab = []
    new_string = ''
    for i_line in range(0, len(file_handler)-2):
        for i_b in range(0, len(file_handler[i_line+2].strip())):
            # print(i_b+1+size*i_line + size*size*time)
            if file_handler[2+i_line][i_b] == '0':
                value_tab.append((-1)*(i_b+1+size*i_line + size*size*time))
                new_string += '0'
            if file_handler[2+i_line][i_b] == '1':
                new_string += '1'
                value_tab.append((i_b+1+size*i_line + size*size*time))
        new_string += '\n'

    # print(new_string)
    # print(value_tab)
    return value_tab, size, time

def fix_values_in_encoding(value_tab, nr_of_variables, nr_of_clauses, encoding):

    nr_of_clauses = nr_of_clauses + len(value_tab)
    for i_value in range(0,len(value_tab)):
        encoding += '%d 0\n'%(value_tab[i_value])

    return nr_of_variables, nr_of_clauses, encoding

def add_cycle_constraints(size, time, nr_of_variables, nr_of_clauses, encoding):
    nr_of_clauses = nr_of_clauses + size*size*2

    for i_bit in range(0,size*size):
        encoding += '-%d %d 0\n'%(i_bit+1, i_bit + 1 + size*size*time)
        encoding += '%d -%d 0\n'%(i_bit+1, i_bit + 1 + size*size*time)

    return nr_of_variables, nr_of_clauses, encoding

def create_cnf(nr_of_variables, nr_of_clauses, encoding, cnf_name):

    file_handler = open(cnf_name,'w')
    file_handler.write('p cnf %d %d\n'%(nr_of_variables, nr_of_clauses))
    file_handler.write(encoding)
    file_handler.close()

    return cnf_name

def get_solution(cnf_sol, out_file, size, time):

    file_handler = open(cnf_sol,'r').readlines()
    solution = []
    # res = True
    for i_line in file_handler:
        if i_line[0] == 'v':
            splited = (i_line[1:].strip()).split(' ')
            solution += splited
        if 'UNSAT' in i_line:
            return False

    out_string = ''
    for i_b in range(0,size*size*(time+1)):
        if i_b > 0 and i_b % size == 0:
            out_string += '\n'
        if i_b > 0 and i_b % (size*size) == 0:
            out_string += '--->\n'

        if '-' in solution[i_b]:
            out_string += '0'
        else:
            out_string += '1'


    file_out = open(out_file,'w')
    file_out.write(out_string)
    file_out.close()

    return True

def find_origin_of_gol(inputfile, cycle, solver, trans, show):

    value_tab, size, time = read_output_value(file_in = inputfile)

    nr_of_variables, nr_of_clauses, encoding = grid_over_time(size = size,
                                                              time = time,
                                                              file_cnf = trans)

    nr_of_variables, nr_of_clauses, encoding = fix_values_in_encoding(value_tab = value_tab,
                                                                      nr_of_variables = nr_of_variables,
                                                                      nr_of_clauses = nr_of_clauses,
                                                                      encoding = encoding)
    if cycle:
        nr_of_variables, nr_of_clauses, encoding = add_cycle_constraints(size = size,
                                                                         time = time,
                                                                         nr_of_variables = nr_of_variables,
                                                                         nr_of_clauses = nr_of_clauses,
                                                                         encoding = encoding)
    cnf_name = create_cnf(nr_of_variables = nr_of_variables,
                          nr_of_clauses = nr_of_clauses,
                          encoding = encoding,
                          cnf_name = inputfile+'.cnf')

    cnf_sol = cnf_name+'.out'
    print('Solving SAT problem : %s %s > %s'%(solver, cnf_name, cnf_sol))
    os.system('%s %s > %s'%(solver, cnf_name, cnf_sol))

    res = get_solution(cnf_sol = cnf_sol,
                        out_file = inputfile[:-3]+'.out',
                        size = size,
                        time = time)

    if res == False:
        print('No solution.')
    if res == True:
        print('Success!!!')

    if res and show:
        print('Printing solution in:')
        for i_p in range(1,4):
            ts.sleep(0.5)
            print('%d'%(i_p))
        if cycle:
            gol.show_gol(size = size, file_ini = inputfile[:-3]+'.out',time = 5*time-1, updateInterval = 500, repeat = False)
        else:
            gol.show_gol(size = size, file_ini = inputfile[:-3]+'.out',time = time-1, updateInterval = 700, repeat = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conway's Game of Life and Bounded Model Checking")

    parser.add_argument("-i", "--inputfile", type=str, help="File with fixed last time frame")
    parser.add_argument("-c", "--cycle", type=bool, default = False, help="Flag if searching for fixed point")
    parser.add_argument("-p", "--print", type=bool, default = True, help="Show solution")
    parser.add_argument("-s", "--solver", type=str, default = 'kissat', help="Full path to SAT-solver")
    parser.add_argument("-t", "--trans", type=str, default = 'transfunc.cnf', help="Path to CNF encoding of transition function")

    args = parser.parse_args()
    find_origin_of_gol(inputfile = args.inputfile, cycle = args.cycle, solver = args.solver, trans = args.trans, show = args.print)
    # compare_rsps(file_rsp_one = args.rsp1, file_rsp_two = args.rsp2, test_type  = args.test )
