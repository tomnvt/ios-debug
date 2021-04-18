//
//  AppDelegate.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    func presentFirstScreen(application: UIApplication) {
        let window = application.keyWindow ?? UIWindow()
        let navigationController = UINavigationController(nibName: nil, bundle: nil)
        navigationController.isNavigationBarHidden = true
        self.window = window
        self.window?.rootViewController = ShakableNavigationController() // !!! Don't edit this line while in debug mode !!!
        self.window?.makeKeyAndVisible()
    }
}


// MARK: - Debug mode helper classes
// WARNING: DO NOT ADD ANY PRODUCTION CODE BELLOW THIS LINE
class ShakableNavigationController: UINavigationController {

    override func motionEnded(_ motion: UIEvent.EventSubtype, with event: UIEvent?) {
        if motion == .motionShake {
            present(MockManager(), animated: true, completion: nil)
        }
    }
}


class MockManager: UITableViewController {

    static var cursor = [
        "MockAwesomeRepositoryImpl": [
            "doAwesomeThings()": 0
        ]
    ]

    // swiftlint:disable trailing_comma
    static var settings = [
        "MockAwesomeRepositoryImpl": [
            "doAwesomeThings()": ["Mocked1", "Mocked2", "Mocked3"]
        ]
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
