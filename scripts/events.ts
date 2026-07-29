export interface ValueWithTimings<T> {
    value: T;
    properties: IProperties;
    measurements: IMeasurements;
}
export interface IProperties {
    [name: string]: string;
}
export interface IMeasurements {
    [name: string]: number;
}

// Telemetry has been removed so this extension only communicates with the
// Azure DevOps host. These functions are intentionally no-ops and are kept so
// existing call sites continue to work without sending any data externally.
export function flushNow() {
    // no-op
}

export function trackEvent(_name: string, _properties?: IProperties, _measurements?: IMeasurements) {
    // no-op
}
