FUNCTION_TEMPLATE = """
    func <FUNC_NAME>(<FUNC_PARAMS>) <RETURN_TYPE>{
        switch MockManager.getOption(self, #function) {
        <CASES>
        default: break
        }
        <RETURN>originalInstance.<ORIGINAL_FUNC_CALL>
    }
"""

TEMPLATE = """
// MARK: - Mock implementation
protocol Mock<PROTOCOL>: <PROTOCOL> {}

class Mock<PROTOCOL>Impl: <PROTOCOL> {

    private let originalInstance: <PROTOCOL>

    init(originalInstance: <PROTOCOL>) {
        self.originalInstance = originalInstance
    }
}

extension Mock<PROTOCOL>Impl {

    <FUNCTIONS>
}

import Swinject
func registerMock<PROTOCOL>(to container: Container) {
    container.register(<PROTOCOL>.self) { r in
        Mock<PROTOCOL>Impl(
            originalInstance: r.resolve(<PROTOCOL>Impl.self)!
        )
    }
}
"""

SHAKABLE_NC = """
// MARK: - Debug mode helper classes
// WARNING: DO NOT ADD ANY PRODUCTION CODE BELLOW THIS LINE
class ShakableNavigationController: UINavigationController {

    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        if motion == .motionShake {
            present(MockManager(), animated: true, completion: nil)
        }
    }
}
"""

SHAKABLE_NC_INSTANCE = "ShakableNavigationController() // !!! Don't edit this line while in debug mode !!!"

MOCK_MANAGER_TEMPLATE = """

import Stevia

class MockManager: UITableViewController {

    static var cursor = [
        <MOCK_CURSORS>
    ]

    // swiftlint:disable trailing_comma
    static var settings = [
        <MOCK_SETTINGS>
    ]

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        tableView.reloadData()
    }

    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        let keys = Array(Self.settings.keys)
        return keys[section]
    }

    override func numberOfSections(in tableView: UITableView) -> Int {
        Self.settings.keys.count
    }

    // swiftlint:disable force_unwrapping
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        let keys = Array(Self.settings.keys)
        return Self.settings[keys[section]]?.keys.count ?? 0
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        let currentKeySubkeyPair = getCurrentKeyAndSubKey(for: indexPath)
        let currentCursor = getCurrentCursor(for: indexPath)
        let isMocked = Self.settings[currentKeySubkeyPair.key]![currentKeySubkeyPair.subKey]!
        cell.textLabel?.text = isMocked[currentCursor]
        return cell
    }

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let currentKeySubkeyPair = getCurrentKeyAndSubKey(for: indexPath)
        let options = Self.settings[currentKeySubkeyPair.key]![currentKeySubkeyPair.subKey]!
        let cursor = getCurrentCursor(for: indexPath)
        if cursor < options.count - 1 {
            Self.cursor[currentKeySubkeyPair.key]![currentKeySubkeyPair.subKey] = cursor + 1
        } else {
            Self.cursor[currentKeySubkeyPair.key]![currentKeySubkeyPair.subKey] = 0
        }
        tableView.reloadData()
    }

    func getCurrentCursor(for indexPath: IndexPath) -> Int {
        let keyAndSubkey = getCurrentKeyAndSubKey(for: indexPath)
        return Self.cursor[keyAndSubkey.key]![keyAndSubkey.subKey]!
    }

    func getCurrentKeyAndSubKey(for indexPath: IndexPath) -> (key: String, subKey: String) {
        let keys = Array(Self.settings.keys)
        let currentKey = keys[indexPath.section]
        return (key: currentKey, subKey: Array(Self.settings[currentKey]!.keys)[indexPath.row])
    }

    static func getOption(_ target: Any, _ functionName: String) -> String {
        let className = Mirror(reflecting: target).description.split(separator: " ").last!
        let cursor = MockManager.cursor[String(className)]![functionName]!
        let options = MockManager.settings[String(className)]![functionName]!
        return options[cursor]
    }
}
"""

MOCK_MANAGER_SETTINGS_TEMPLATE = """"<PROTOCOL>": [
    <FUNCTION_SETTINGS>
        ]"""

FUNCTION_SETTINGS_TEMPLATE = """        "<FUNCTION_ANNOTATION>": <SETTINGS_VALUES>"""
