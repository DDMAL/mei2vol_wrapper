import mei2volpiano
from rodan.jobs.base import RodanTask
from django.conf import settings as rodan_settings
import json


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
    enabled = False  # for now
    category = "Type conversion"
    interactive = False

    input_port_types = [
        {
            "name": "MEI",
            "minimum": 1,
            "maximum": 100,  # magic number, let us know what the max is TODO
            "resource_types": ["application/mei+xml"],  # double check dir
        }
    ]

    output_port_types = [
        {
            "name": "Volpiano",
            "minimum": 1,
            "maximum": 100,
            "resource_types": ["application/text"],
        }
    ]

    def run_my_task(self, inputs, settings, outputs):
        """Skeleton of task runner. Not complete."""
        if "@done" not in settings:
            return self.WAITING_FOR_INPUT()
        # Testing with single input.
        volpiano = []

        with open(inputs["MEI"][0]["resource_path"], "r") as f:
            volpiano.append(mei2volpiano.MEItoVolpiano.convert_mei_volpiano(f))

        outfile_path = outputs["Volpiano"][0]["resource_path"]
        outfile = open("volpiano.txt", "w")
        outfile.write(volpiano[0])
        outfile.close()
