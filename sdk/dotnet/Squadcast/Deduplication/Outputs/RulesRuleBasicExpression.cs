// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Deduplication.Outputs
{

    [OutputType]
    public sealed class RulesRuleBasicExpression
    {
        /// <summary>
        /// left hand side dropdown value
        /// </summary>
        public readonly string Lhs;
        /// <summary>
        /// operator
        /// </summary>
        public readonly string Op;
        /// <summary>
        /// right hand side value
        /// </summary>
        public readonly string Rhs;

        [OutputConstructor]
        private RulesRuleBasicExpression(
            string lhs,

            string op,

            string rhs)
        {
            Lhs = lhs;
            Op = op;
            Rhs = rhs;
        }
    }
}
