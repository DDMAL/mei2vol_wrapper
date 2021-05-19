from rodan.jobs.base import RodanTask

# potentially needed
# from django.conf import settings as rodan_settings
import json

# avoid python3 conflict in Rodan
try:
    from mei2volpiano import MEI2Volpiano
except(ImportError):
    pass

# Rodan job
class MEI2Vol(RodanTask):
    name = "MEI2Volpiano"
    author = "Ravi Raina, Kemal Kongar, & Gabrielle Halpin"
    description = "Converts MEI or XML files into volpiano strings."
    settings = {
        "title": "Parameters",
        "type": "object",
        "job_queue": "Python3",
        "properties": {"Output": {"type": "string", "default": ""}},
    }
    enabled = True
    category = "Type conversion"
    interactive = False

    input_port_types = [
        {
            "name": "MEI",
            "minimum": 1,
            "maximum": 1, 
            "resource_types": ["application/mei+xml"],
            #"is_list": True
        }
    ]

    output_port_types = [
        {
            "name": "Volpiano",
            "minimum": 1,
            "maximum": 1,
            "resource_types": ["text/plain"],
            #"is_list": True
        }
    ]

    def run_my_task(self, inputs, settings, outputs):
        # Testing with single input.
        volpianos = []
        mei_names = []
        for input_type in inputs: 
            for element in inputs[input_type]:
                with open(element["resource_path"], "r") as infile:
                    mei_names.append(infile)
                    volpianos.append(MEI2Volpiano.convert_mei_volpiano(infile))

        for output_type in outputs:
            for i, output in enumerate(outputs[output_type]):
                with open(output["resource_path"], "w") as outfile:
                    outfile.write(mei_names[i])
                    outfile.write(volpianos[i])
                    outfile.write("\n")

        return True
