import MEI2Volpiano from mei2volpiano
from rodan.jobs.base import RodanTask
from django.conf import settings as rodan_settings
import json


class MEI2Vol(RodanTask):
    name = "MEI2Volpiano"
    author = "Ravi Raina, Kemal Kongar, & Gabrielle Halpin"
    description = "Converts MEI or XML files into volpiano strings."
    settings = {
        # not complete till working on it
        "title": "Parameters",
        "type": "object",
        "job_queue": "Python3",
        "properties": {"Output": {"type": "string", "default": ""}},
    }
    enabled = False  # for now
    category = "Type conversion"
    interactive = False

    input_port_types = [
        {
            "name": "MEI",
            "minimum": 1,
            "maximum": 0, 
            "resource_types": ["application/mei+xml"],  # double check dir
            "is_list": True
        }
    ]

    output_port_types = [
        {
            "name": "Volpiano",
            "minimum": 1,
            "maximum": 0,
            "resource_types": ["application/text"],
            "is_list": True
        }
    ]

    def run_my_task(self, inputs, settings, outputs):
        """Skeleton of task runner. Not complete."""
        # Testing with single input.
        volpianos = []
        mei_names = []
        for input_type in inputs: 
            for element in inputs[input_type]:
                with open(element["resource_path"], "r") as infile:
                    mei_names.append(infile)
                    volpianos.append(MEItoVolpiano.convert_mei_volpiano(infile))

        for output_type in outputs:
            for i, output in enumerate(outputs[output_type]):
                with open(output["resource_paht"], "w") as outfile:
                    outfile.write(mei_names[i])
                    outfile.write(volpianos[i])
                    outfile.write("\n")

        return True
