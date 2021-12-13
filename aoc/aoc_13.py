from typing import List, Set, Tuple

INPUT_FILEPATH = 'aoc_13_input.txt'


def fold_manual(dots: Set, fold: Tuple[int]) -> Set:
    folded_dots = set()
    is_x_fold = fold[0] > 0
    is_y_fold = fold[1] > 0
    
    for dot in dots:
        if is_x_fold and not is_y_fold:
            if dot[0] > fold[0]:
                x_fold = 2 * fold[0] - dot[0]
                folded_dots.add((x_fold, dot[1]))
            else:
                folded_dots.add(dot)
        elif is_y_fold and not is_x_fold:
            if dot[1] > fold[1]:
                y_fold = 2 * fold[1] - dot[1]
                folded_dots.add((dot[0], y_fold))
            else:
                folded_dots.add(dot)
        else:
            raise BaseException("Invalid folding instruction.")
            
    return folded_dots


def main():
    ### part 1
    dotset = set()
    folds = []

    with open(INPUT_FILEPATH, 'r') as fstream:
        for dotline in fstream:
            pair = dotline.split(',')
            if len(dotline) > 1:
                int_pair = tuple(map(int, pair))
                dotset.add(int_pair)
            else:
                print("Got all them dots!")
                break;

        for foldline in fstream:
            fold = foldline.split()[2].split("=")
            assert len(fold) == 2
            if fold[0] == "x":
                fold_val = (int(fold[1]), 0)
            elif fold[0] == "y":
                fold_val = (0, int(fold[1]))
            else:
                raise BaseException("Invalid folding instruction.")

            folds.append(fold_val)

        print("Got all them folds!")
        
    
    print(f"Number of dots before first fold: {len(dotset)}")
        
    first_fold = folds[0]
    print(f"Folding only the first fold: {first_fold}")
    
    result_dots = fold_manual(dotset, first_fold)
    print(f"Number of result dots after first fold: {len(result_dots)}")
    
    
    ### part 2
    final_dots = dotset
    for fold in folds:
        final_dots = fold_manual(final_dots, fold)
        
    print(f"Number of dots after all ({len(folds)}) folds: {len(final_dots)}")

    max_vals: Tuple[int] = (max(final_dots,key=lambda item:item[0])[0],  max(final_dots,key=lambda item:item[1])[1])
    
    result_string = ""
    
    for row in range(0, max_vals[1]+1):
        for column in range(0, max_vals[0]+1):
            if (column, row) in final_dots:
                result_string += '#'
            else:
                result_string += '.'
        result_string += '\n'
    
    print("\nActivation Code:\n")
    print(result_string)
            
        
            
if __name__ == "__main__":
    main()
