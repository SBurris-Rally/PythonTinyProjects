#! /bin/bash

# size=large

# python3 -m cProfile apples_mine.py  -v i input/$size_file.txt > apples_mine_cprofile_$size.txt
# python3 -m cProfile apples_mine.py  -v i input/fox.txt > apples_mine_cprofile_fox.txt

# python3 -m memory_profiler apples_mine.py  -v i input/fox.txt > apples_mine_memory_profiler_fox.txt

python3 -m cProfile apples_mine.py -v i input/large_file.txt > apples_mine_cprofile.txt
python3 -m cProfile apples_1_for_loop.py -v i input/large_file.txt > apples_1_for_loop_cprofile.txt
python3 -m cProfile apples_2_str_replace.py -v i input/large_file.txt > apples_2_str_replace_cprofile.txt
python3 -m cProfile apples_3_str_translate.py -v i input/large_file.txt > apples_3_str_translate_cprofile.txt
python3 -m cProfile apples_4_list_comprehension.py -v i input/large_file.txt > apples_4_list_comprehension_cprofile.txt
python3 -m cProfile apples_5_list_comp_function.py -v i input/large_file.txt > apples_5_list_comp_function_cprofile.txt
python3 -m cProfile apples_6_map.py -v i input/large_file.txt > apples_6_map_cprofile.txt
python3 -m cProfile apples_7_map_with_function.py > -v i input/large_file.txt apples_7_map_with_function_cprofile.txt
python3 -m cProfile apples_8_regex.py -v i input/large_file.txt > apples_8_regex_cprofile.txt
