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

        for element in inputs["MEI"]: # This may not work, check dictionary. 
            with open(element[0]["resource_path"], "r") as f:
                volpianos.append(MEItoVolpiano.convert_mei_volpiano(f))
                f.close()
 
        outfile_path = None
        for i, entry in enumerate(volpianos): # Likewise, check dictionary.
            outfile_path = outputs["Volpiano"][i]["resource_path"] # May need to point to [0]
            outfile = open(outfile_path, "w+")
            outfile.write(volpianos[i])
            outfile.close()

        return True
