import argparse
import subprocess
import shlex
import os
import pathlib

def cmd(cmd, stdout=None, stderr=None, setenv={}):
        env = dict(os.environ)
        for key, value in setenv.items():
            env[key] = value 
        output = subprocess.run(shlex.split(cmd), stdout=stdout, text=True, env=env)

        if stdout == subprocess.PIPE:
            return f"{output.stdout.strip()}"
        else:
            return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
    
    verible_args_list = []
    verible_args_list = [
        "--column_limit",
        "--indentation_spaces 4",
        "--assignment_statement_alignment flush-left", # align,flush-left,preserve,infer}; default: infer
        "--case_items_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--class_member_variable_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--compact_indexing_and_selections true", # default: true;
        "--distribution_items_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--enum_assignment_statement_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--expand_coverpoints false", # default: false;
        "--formal_parameters_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--formal_parameters_indentation indent", # {indent,wrap}); default: wrap;
        "--module_net_variable_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--named_parameter_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--named_parameter_indentation indent", # {indent,wrap}); default: wrap;
        "--named_port_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--named_port_indentation indent", # {indent,wrap}); default: wrap;
        "--port_declarations_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--port_declarations_indentation indent", # {indent,wrap}); default: wrap;
        "--port_declarations_right_align_packed_dimensions false", # default: false;
        "--port_declarations_right_align_unpacked_dimensions false", # default: false;
        "--struct_union_members_alignment flush-left", # {align,flush-left,preserve,infer}); default: infer;
        "--try_wrap_long_lines false", # default: false;
    ]
    verible_args = " ".join(verible_args_list)
    files = args.filenames
    for file in files:
        if pathlib.Path(file).suffix in [".sv", ".v"]:
            # print(f"{pathlib.Path().cwd()/file}")
            cmd(f"verible-verilog-format --inplace {verible_args} {file}")

if __name__ == "__main__":
    main()