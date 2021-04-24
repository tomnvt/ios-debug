//
//  AwesomeRepository.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import Foundation
import RxSwift

protocol AwesomeRepository {

    typealias Nothing = Void

    var someVariable: String { get }

    func doAwesomeThings()
    func doGenericAwesomeThings<T>(type: T.Type)
    func doAwesomeThingsWithTupleParameter(tupleList: [(first: String, second: String)])
    // MARK: - This is just a mark
    func doAwesomeThingsAndReturnSingle() -> Single<String>
    /// Docs
    /// More docs
    func doAwesomeThingsWithDocs()

    func getLatestAndMinimal() -> Single<(latest: String, minimal: String)>
}

// MARK: - Mock implementation init
protocol MockAwesomeRepository: AwesomeRepository {}

class MockAwesomeRepositoryImpl: AwesomeRepository {

    private let originalInstance: AwesomeRepository

    init(originalInstance: AwesomeRepository) {
        self.originalInstance = originalInstance
    }
}

extension MockAwesomeRepositoryImpl {

    
    func doAwesomeThings() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThings()
    }

    
    func doGenericAwesomeThings<T>(type: T.Type) {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doGenericAwesomeThings(type: type)
    }

    
    func doAwesomeThingsWithTupleParameter(tupleList: [(first: String, second: String)]) {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThingsWithTupleParameter(tupleList: tupleList)
    }

    
    func doAwesomeThingsAndReturnSingle() -> Single<String> {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        case "Mocked4": break
        default: break
        }
        return originalInstance.doAwesomeThingsAndReturnSingle()
    }

    
    func doAwesomeThingsWithDocs() {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        originalInstance.doAwesomeThingsWithDocs()
    }

    
    func getLatestAndMinimal() -> Single<(latest: String, minimal: String)> {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        return originalInstance.getLatestAndMinimal()
    }

}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}
