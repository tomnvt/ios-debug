//
//  AwesomeRepositoryImpl.swift
//  DebugModeTestApp
//
//  Created by Tom Novotny on 17.04.2021.
//

import Foundation
import RxSwift

class AwesomeRepositoryImpl {

}

// MARK: - Protocol conformance
extension AwesomeRepositoryImpl: AwesomeRepository {
    
    var someVariable: String { "" }

    func doAwesomeThings() {
        print("Doing awesome things")
    }

    func doGenericAwesomeThings<T>(type: T.Type) {
        print("Doing awesome things with \(type)")
    }

    func doAwesomeThingsWithTupleParameter(tupleList: [(first: String, second: String)]) {
        print("Doing awesome things with \(tupleList)")
    }

    func doAwesomeThingsAndReturnSingle() -> Single<String> {
        return .just("Doing awesome things")
    }

    func doAwesomeThingsWithDocs() {
        print("Doing awesome things")
    }

    func getLatestAndMinimal() -> Single<(latest: String, minimal: String)> {
        Observable.empty().asSingle()
    }

    func justAnotherFunction() -> Bool {
        true
    }
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
        case "Mocked4": break
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

    func justAnotherFunction() -> Bool {
        switch MockManager.getOption(self, #function) {
        case "Mocked1": break
        case "Mocked2": break
        case "Mocked3": break
        default: break
        }
        return originalInstance.justAnotherFunction()
    }
}

import Swinject
func registerMockAwesomeRepository(to container: Container) {
    container.register(AwesomeRepositoryImpl.self) { r in
        AwesomeRepositoryImpl()
    }
    container.register(AwesomeRepository.self) { r in
        MockAwesomeRepositoryImpl(
            originalInstance: r.resolve(AwesomeRepositoryImpl.self)!
        )
    }
}
