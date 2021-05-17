from rodan.jobs.base import RodanTask


class MEI2Vol(RodanTask):
    name = "MEI2Volpiano"
    authors = "DDMAL"
    description = "Converts MEI or XML files into volpiano strings."
    # settings TODO
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
