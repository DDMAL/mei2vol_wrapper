import mei2volpiano
from rodan.jobs.base import RodanTask


class MEI2Vol(RodanTask):
    name = "MEI2Volpiano"
    author = "Ravi Raina, Kemal Kongar, & Gabrielle Halpin"
    description = "Converts MEI or XML files into volpiano strings."
    settings = {"job_queue": "Python3"}
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
        '''Skeleton of task runner. Not complete.
        '''
        # Testing with single input.
        volpianos = []

        for element in inputs["MEI"]:
            with open (element[0]["resource_path"], "r") as f:
              volpianos.append(mei2volpiano.MEItoVolpiano.convert_mei_volpiano(f))
              f.close()  
        
        outfile_path = None
        for i, entry in enumerate(volpianos):
            outfile_path = outputs["Volpiano"][i]["resource_path"]
            outfile = open(outfile_path, "w+")
            outfile.write(volpianos[i])
            outfile.close()

        return True
