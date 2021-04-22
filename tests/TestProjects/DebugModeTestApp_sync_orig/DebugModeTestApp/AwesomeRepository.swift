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

    func doGenericAwesomeThings<T>(type: T.Type)
    func doAwesomeThingsWithTupleParameter(tupleList: [(first: String, second: String)])
    // MARK: - This is just a mark
    func doAwesomeThingsAndReturnSingle() -> Single<String>
    /// Docs
    /// More docs
    func doAwesomeThingsWithDocs()

    func getLatestAndMinimal() -> Single<(latest: String, minimal: String)>
    func justAnotherFunction(param: Bool) -> Bool
}
