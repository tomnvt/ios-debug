import re
from pprint import pprint
from collections import defaultdict


def get_mock_functions_variants(protocol_to_mocked_contents):
    result = {}
    for entity in protocol_to_mocked_contents:
        result[entity] = defaultdict(str)
        mocked_content = protocol_to_mocked_contents[entity]
        mocked_extension = re.findall("extension [\s\S]+?\n}", mocked_content)[0]
        functions_split = mocked_extension.split("func ")[1:]
        for function in functions_split:
            function_name = re.findall("([\s\S]+?) {", function)[0]
            cases = re.findall("case (.*):", function)
            result[entity][function_name] = cases
    return result


test = {
    "AwesomeRepository": '\n\n\n\nprotocol MockAwesomeRepository: AwesomeRepository {}\n\nclass MockAwesomeRepositoryImpl: AwesomeRepository {\n\n    var someVariable: String { originalInstance.someVariable }\n\n    private let originalInstance: AwesomeRepository\n\n    init(originalInstance: AwesomeRepository) {\n        self.originalInstance = originalInstance\n    }\n}\n\nextension MockAwesomeRepositoryImpl {\n\n    \n    func doAwesomeThings() {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        case "Mocked4": break\n        default: break\n        }\n        originalInstance.doAwesomeThings()\n    }\n\n    \n    func doGenericAwesomeThings<T>(type: T.Type) {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        default: break\n        }\n        originalInstance.doGenericAwesomeThings(type: type)\n    }\n\n    \n    func doAwesomeThingsWithTupleParameter(tupleList: [(first: String, second: String)]) {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        default: break\n        }\n        originalInstance.doAwesomeThingsWithTupleParameter(tupleList: tupleList)\n    }\n\n    \n    func doAwesomeThingsAndReturnSingle() -> Single<String> {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        default: break\n        }\n        return originalInstance.doAwesomeThingsAndReturnSingle()\n    }\n\n    \n    func doAwesomeThingsWithDocs() {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        default: break\n        }\n        originalInstance.doAwesomeThingsWithDocs()\n    }\n\n    \n    func getLatestAndMinimal() -> Single<(latest: String, minimal: String)> {\n        switch MockManager.getOption(self, #function) {\n        case "Mocked1": break\n        case "Mocked2": break\n        case "Mocked3": break\n        default: break\n        }\n        return originalInstance.getLatestAndMinimal()\n    }\n\n}\n\nimport Swinject\nfunc registerMockAwesomeRepository(to container: Container) {\n    container.register(AwesomeRepository.self) { r in\n        MockAwesomeRepositoryImpl(\n            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!\n        )\n    }\n}\n'
}

pprint(get_mock_functions_variants(test))
