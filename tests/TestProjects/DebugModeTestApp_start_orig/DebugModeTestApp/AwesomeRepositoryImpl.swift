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
        Single.just(("Awesome", "Things"))
    }
}
